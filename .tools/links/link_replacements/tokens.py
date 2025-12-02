"""Straightforward token replacement helpers."""

from __future__ import annotations

import os
import re
from pathlib import Path
from threading import RLock
from typing import Callable, Dict, Iterable, Optional

from broken_links.common import normalize_string
from .mentions import find_dynamic_target, format_dynamic_link_text


HARDCODED_HANDLERS: Dict[str, Dict[str, object]] = {}
TRIPLE_BRACE_PATTERN = re.compile(r"\{\{\{([^{}]+)\}\}\}")

def _find_basename(md_files: Iterable[str], basename: str) -> Optional[Path]:
    """Return the first markdown file whose basename matches the provided name."""

    for candidate in md_files:
        if os.path.basename(candidate) == basename:
            return Path(candidate)
    return None

_SIMPLE_CONTENT_CACHE: Dict[str, Dict[str, object]] = {}
_SIMPLE_CACHE_LOCK = RLock()
LINK_PATTERN = re.compile(r"\[[^\]]+?\]\(<[^>]+?>\)", re.DOTALL)
PATTERN_NEEDLES: Dict[int, str] = {}
TOKEN_LITERAL_EXTRACT = re.compile(r"`\??([^`]+)`\??")


def _build_dot_function_index(md_files: Iterable[str]) -> Dict[str, Path]:
    """Map normalized dot-function tokens (e.g. '.UUID') to canonical files."""

    index: Dict[str, Path] = {}

    def maybe_store(key: str, path: Path) -> None:
        if not key:
            return

        existing = index.get(key)
        if existing is None:
            index[key] = path
            return

        existing_score = (len(existing.parts), str(existing))
        candidate_score = (len(path.parts), str(path))
        if candidate_score < existing_score:
            index[key] = path

    for path_str in md_files:
        path = Path(path_str)
        if path.suffix.lower() != ".md":
            continue

        stem = path.stem
        if "ⓕ" not in stem:
            continue

        left, sep, right = stem.partition("ⓕ")
        if not sep:
            continue

        token_left = normalize_string(left)
        token_right = normalize_string(right)
        if not token_left:
            continue

        maybe_store(token_left, path)
        if token_right:
            maybe_store(f"{token_left}{token_right}", path)

    return index


def _register_literal_pattern(pattern: re.Pattern[str], token_literal: str) -> re.Pattern[str]:
    PATTERN_NEEDLES[id(pattern)] = token_literal
    return pattern


def clear_simple_replacer_cache() -> None:
    """Reset cached file contents used by simple token replacers."""

    with _SIMPLE_CACHE_LOCK:
        _SIMPLE_CONTENT_CACHE.clear()


def register_hardcoded(
    token_key: str,
    *,
    replacement: str,
    token_label: str,
) -> Callable[[Callable[[Iterable[str]], int]], Callable[[Iterable[str]], int]]:
    """Register a token replacer that is backed by a static replacement string."""

    def decorator(func: Callable[[Iterable[str]], int]) -> Callable[[Iterable[str]], int]:
        HARDCODED_HANDLERS[token_key] = {
            "replacement": replacement,
            "token_label": token_label,
            "func": func,
        }
        return func

    return decorator


def _get_cached_entry(path: Path) -> Optional[Dict[str, object]]:
    key = str(path)
    with _SIMPLE_CACHE_LOCK:
        entry = _SIMPLE_CONTENT_CACHE.get(key)
    if entry is not None:
        return entry

    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return None

    entry = {"content": text, "link_spans": None, "lower": None}
    with _SIMPLE_CACHE_LOCK:
        _SIMPLE_CONTENT_CACHE[key] = entry
    return entry


def _replace_simple(
    md_files: Iterable[str],
    pattern: re.Pattern[str],
    replacement: str,
    *,
    needle: Optional[str] = None,
) -> int:
    """Replace occurrences of pattern with replacement while respecting existing links."""

    total = 0
    for md_file in md_files:
        path = Path(md_file)
        entry = _get_cached_entry(path)
        if entry is None:
            continue

        content = entry.get("content")
        if not isinstance(content, str) or "{{" not in content:
            continue

        if needle is None:
            needle = PATTERN_NEEDLES.get(id(pattern))
            if needle is None:
                match = TOKEN_LITERAL_EXTRACT.search(pattern.pattern)
                if match:
                    candidate = match.group(1)
                    needle = re.sub(r"\\(.)", r"\1", candidate)
                    PATTERN_NEEDLES[id(pattern)] = needle

        if needle:
            if needle in content:
                pass
            else:
                lower = entry.get("lower")
                if lower is None:
                    lower = content.lower()
                    entry["lower"] = lower
                if needle.lower() not in lower:
                    continue

        if not pattern.search(content):
            continue

        link_spans = entry.get("link_spans")
        if link_spans is None:
            link_spans = [m.span() for m in LINK_PATTERN.finditer(content)]
            entry["link_spans"] = link_spans

        changes = 0

        if link_spans:
            spans = tuple(link_spans)

            def _repl(m: re.Match[str]) -> str:
                nonlocal changes
                pos = m.start()
                for a, b in spans:
                    if a <= pos < b:
                        return m.group(0)
                changes += 1
                return replacement
        else:
            def _repl(m: re.Match[str]) -> str:
                nonlocal changes
                changes += 1
                return replacement

        new_content = pattern.sub(_repl, content)
        if not changes:
            continue

        try:
            path.write_text(new_content, encoding="utf-8")
        except Exception:
            continue

        entry["content"] = new_content
        entry["link_spans"] = None
        entry["lower"] = None
        total += changes

    return total


def _simple_pattern_for(token_literal: str) -> re.Pattern[str]:
    """Build a simple regex pattern matching {{ `Token` }} variants for a token literal."""

    pattern = rf"\{{\{{[\s\u00A0\u200B\u200C\u200D]*`?{re.escape(token_literal)}`?[\s\u00A0\u200B\u200C\u200D]*\}}\}}"
    compiled = re.compile(pattern, re.IGNORECASE)
    PATTERN_NEEDLES[id(compiled)] = token_literal
    return compiled


def _make_hardcoded_replacer(func_name: str, token_literal: str, token_key: str, replacement: str, token_label: str):
    """Dynamically create and register a simple hardcoded replacer.

    The created function will be available in module globals under `func_name`
    and also registered in HARDCODED_HANDLERS under `token_key`.
    """

    pattern = _simple_pattern_for(token_literal)

    def replacer(md_files: Iterable[str]) -> int:
        return _replace_simple(md_files, pattern, replacement, needle=token_literal)

    replacer.__name__ = func_name
    globals()[func_name] = replacer
    HARDCODED_HANDLERS[token_key] = {"func": replacer, "replacement": replacement, "token_label": token_label}
    return replacer


_DOT_FUNCTION_PATTERN = re.compile(
    r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?\.(\w+(?:[\s\u00A0\u200B\u200C\u200D]+\w+)*)`?[\s\u00A0\u200B\u200C\u200D]*\}\}"
)


PLACEHOLDER_REPLACEMENT = "[Placeholder 🧠](<Holder 🧠.md>)"
HOLDER_REPLACEMENT = "[Holder 🧠](<Holder 🧠.md>)"
HOSTS_REPLACEMENT = "[Host 🤗 domains](<🤗🎭 Host role.md>)"
HOST_REPLACEMENT = "[Host 🤗 domain](<🤗🎭 Host role.md>)"
SCRIPT_REPLACEMENT = "[Script 📃](<Script 📃.md>)"
SCRIPTS_REPLACEMENT = "[Scripts 📃](<Script 📃.md>)"
MANIFEST_REPLACEMENT = "[Manifest 📜](<📜 Manifest.md>)"
MANIFESTS_REPLACEMENT = "[Manifests 📜](<📜 Manifest.md>)"
COMMAND_REPLACEMENT = "[Command ⌘](<Command ⌘.md>)"
COMMANDS_REPLACEMENT = "[Commands ⌘](<Command ⌘.md>)"
BROKER_REPLACEMENT = "[Broker 🤵 domain](<🤵 Broker 🤲 helper.md>)"
SELLER_REPLACEMENT = "[Seller 🎭 domain](<💵🎭 Seller role.md>)"
SELLERS_REPLACEMENT = "[Seller 🎭 domains](<💵🎭 Seller role.md>)"
BILLER_REPLACEMENT = "[Biller 🤝 domain](<🤝🤲 Biller helper.md>)"
BILLERS_REPLACEMENT = "[Biller 🤝 domains](<🤝🤲 Biller helper.md>)"
SUBSCRIBER_REPLACEMENT = "[Subscriber 🔔 domain](<../Subscribers 🔔/🔔🎭 Subscriber role.md>)"
SUBSCRIBERS_REPLACEMENT = "[Subscriber 🔔 domains](<../Subscribers 🔔/🔔🎭 Subscriber role.md>)"
STREAMER_REPLACEMENT = "[Streamer 🌬️ domain](<🌬️🎭 Streamer role.md>)"
STREAMERS_REPLACEMENT = "[Streamer 🌬️ domains](<🌬️🎭 Streamer role.md>)"
CONSUMER_REPLACEMENT = "[Consumer 💼 domain](<💼🎭 Consumer role.md>)"
CONSUMERS_REPLACEMENT = "[Consumer 💼 domains](<💼🎭 Consumer role.md>)"
WALLET_REPLACEMENT = "[Wallet 🧑‍🦰 app](<🧑‍🦰 Wallet 🛠️ app.md>)"
WALLETS_REPLACEMENT = "[Wallet 🧑‍🦰 apps](<🧑‍🦰 Wallet 🛠️ app.md>)"
GRAPH_REPLACEMENT = "[Graph 🕸 domain](<🕸🤲 Graph helper.md>)"
GRAPHS_REPLACEMENT = "[Graph 🕸 domains](<🕸🤲 Graph helper.md>)"


@register_hardcoded("placeholder", replacement=PLACEHOLDER_REPLACEMENT, token_label="Placeholder")
def replace_placeholder_tokens(md_files):
    pattern = _simple_pattern_for("Placeholder")
    return _replace_simple(md_files, pattern, PLACEHOLDER_REPLACEMENT)


@register_hardcoded("holder", replacement=HOLDER_REPLACEMENT, token_label="Holder")
def replace_holder_tokens(md_files):
    pattern = _simple_pattern_for("Holder")
    return _replace_simple(md_files, pattern, HOLDER_REPLACEMENT)


def replace_msg_tokens(md_files):
    pattern = _simple_pattern_for("$.Msg")
    # Use the holder file for $.Msg (emoji then token then '🧠 holder')
    replacement = "[`$.Msg` 🧠 holder](<📨 $.Msg 🧠 holder.md>)"
    return _replace_simple(md_files, pattern, replacement, needle="$.Msg")


@register_hardcoded("hosts", replacement=HOSTS_REPLACEMENT, token_label="Hosts")
def replace_hosts_tokens(md_files):
    pattern = _simple_pattern_for("Hosts")
    return _replace_simple(md_files, pattern, HOSTS_REPLACEMENT)


@register_hardcoded("host", replacement=HOST_REPLACEMENT, token_label="Host")
def replace_host_tokens(md_files):
    pattern = _simple_pattern_for("Host")
    return _replace_simple(md_files, pattern, HOST_REPLACEMENT)


@register_hardcoded("hosted", replacement='[Hosted 📦 domain](<📦👥 Hosted domain.md>)', token_label="Hosted")
def replace_hosted_tokens(md_files):
    pattern = _simple_pattern_for("Hosted")
    return _replace_simple(md_files, pattern, '[Hosted 📦 domain](<📦👥 Hosted domain.md>)')


@register_hardcoded("hosteds", replacement='[Hosted 📦 domains](<📦👥 Hosted domain.md>)', token_label="Hosteds")
def replace_hosteds_tokens(md_files):
    pattern = _simple_pattern_for("Hosteds")
    return _replace_simple(md_files, pattern, '[Hosted 📦 domains](<📦👥 Hosted domain.md>)')


# Hardcoded Trust token
TRUST_REPLACEMENT = "[Trust 🫡](<🫡 Domain Trust.md>)"
@register_hardcoded("trust", replacement=TRUST_REPLACEMENT, token_label="Trust")
def replace_trust_tokens(md_files):
    pattern = _simple_pattern_for("Trust")
    return _replace_simple(md_files, pattern, TRUST_REPLACEMENT)


@register_hardcoded("trusted", replacement='[Trusted 🫡](<🫡 Domain Trust.md>)', token_label="Trusted")
def replace_trusted_tokens(md_files):
    pattern = _simple_pattern_for("Trusted")
    return _replace_simple(md_files, pattern, '[Trusted 🫡](<🫡 Domain Trust.md>)')


@register_hardcoded("holders", replacement='[Holders 🧠](<Holder 🧠.md>)', token_label="Holders")
def replace_holders_tokens(md_files):
    pattern = _simple_pattern_for("Holders")
    return _replace_simple(md_files, pattern, '[Holders 🧠](<Holder 🧠.md>)')


# Hardcoded Helper token
HELPER_REPLACEMENT = "[Helper 🤲 domain](<🤲👥 Helper domain.md>)"
@register_hardcoded("helper", replacement=HELPER_REPLACEMENT, token_label="Helper")
def replace_helper_tokens(md_files):
    pattern = _simple_pattern_for("Helper")
    return _replace_simple(md_files, pattern, HELPER_REPLACEMENT)


@register_hardcoded("helpers", replacement='[Helper 🤲 domains](<🤲👥 Helper domain.md>)', token_label="Helpers")
def replace_helpers_tokens(md_files):
    pattern = _simple_pattern_for("Helpers")
    return _replace_simple(md_files, pattern, '[Helper 🤲 domains](<🤲👥 Helper domain.md>)')


# Hardcoded Hoster tokens
HOSTER_REPLACEMENT = "[Hoster ☁️ helper domain](<☁️🤲 Hoster helper.md>)"
@register_hardcoded("hoster", replacement=HOSTER_REPLACEMENT, token_label="Hoster")
def replace_hoster_tokens(md_files):
    pattern = _simple_pattern_for("Hoster")
    return _replace_simple(md_files, pattern, HOSTER_REPLACEMENT)


@register_hardcoded("hosters", replacement='[Hoster ☁️ helper domains](<☁️🤲 Hoster helper.md>)', token_label="Hosters")
def replace_hosters_tokens(md_files):
    pattern = _simple_pattern_for("Hosters")
    return _replace_simple(md_files, pattern, '[Hoster ☁️ helper domains](<☁️🤲 Hoster helper.md>)')


# Hardcoded Talker tokens
TALKER_REPLACEMENT = "[Talker 😃 helper domain](<😃🤲 Talker helper.md>)"
@register_hardcoded("talker", replacement=TALKER_REPLACEMENT, token_label="Talker")
def replace_talker_helper_tokens(md_files):
    pattern = _simple_pattern_for("Talker")
    return _replace_simple(md_files, pattern, TALKER_REPLACEMENT)


@register_hardcoded("talkers", replacement='[Talker 😃 helper domains](<😃🤲 Talker helper.md>)', token_label="Talkers")
def replace_talkers_helper_tokens(md_files):
    pattern = _simple_pattern_for("Talkers")
    return _replace_simple(md_files, pattern, '[Talker 😃 helper domains](<😃🤲 Talker helper.md>)')


# Hardcoded Finder tokens
FINDER_REPLACEMENT = "[Finder 🔎 domain](<🔎 Finder 🫥 agent.md>)"
@register_hardcoded("finder", replacement=FINDER_REPLACEMENT, token_label="Finder")
def replace_finder_tokens(md_files):
    pattern = _simple_pattern_for("Finder")
    return _replace_simple(md_files, pattern, FINDER_REPLACEMENT)


@register_hardcoded("finders", replacement='[Finder 🔎 domains](<🔎 Finder 🫥 agent.md>)', token_label="Finders")
def replace_finders_tokens(md_files):
    pattern = _simple_pattern_for("Finders")
    return _replace_simple(md_files, pattern, '[Finder 🔎 domains](<🔎 Finder 🫥 agent.md>)')


# Hardcoded Role token
ROLE_REPLACEMENT = "[Role 🎭](<👥🎭 Domain Role.md>)"
@register_hardcoded("role", replacement=ROLE_REPLACEMENT, token_label="Role")
def replace_role_tokens(md_files):
    pattern = _simple_pattern_for("Role")
    return _replace_simple(md_files, pattern, ROLE_REPLACEMENT)


@register_hardcoded("roles", replacement='[Roles 🎭](<👥🎭 Domain Role.md>)', token_label="Roles")
def replace_roles_tokens(md_files):
    pattern = _simple_pattern_for("Roles")
    return _replace_simple(md_files, pattern, '[Roles 🎭](<👥🎭 Domain Role.md>)')


# Hardcoded Async Message(s) tokens
ASYNC_MESSAGES_REPLACEMENT = "[Async Messages 🐌](<Async Messages 🐌.md>)"
@register_hardcoded("asyncmessages", replacement=ASYNC_MESSAGES_REPLACEMENT, token_label="Async Messages")
def replace_async_messages_tokens(md_files):
    pattern = _simple_pattern_for("Async Messages")
    return _replace_simple(md_files, pattern, ASYNC_MESSAGES_REPLACEMENT)


@register_hardcoded("asyncmessage", replacement='[Async Message 🐌](<Async Messages 🐌.md>)', token_label="Async Message")
def replace_async_message_token(md_files):
    pattern = _simple_pattern_for("Async Message")
    return _replace_simple(md_files, pattern, '[Async Message 🐌](<Async Messages 🐌.md>)')


# Hardcoded Sync Request(s) tokens
SYNC_REQUESTS_REPLACEMENT = "[Sync Calls 🚀](<Sync Calls 🚀.md>)"
@register_hardcoded("synccalls", replacement=SYNC_REQUESTS_REPLACEMENT, token_label="Sync Calls")
def replace_sync_requests_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Sync Calls`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, SYNC_REQUESTS_REPLACEMENT)


@register_hardcoded("syncrequest", replacement='[Sync Request 🚀](<Sync Calls 🚀.md>)', token_label="Sync Request")
def replace_sync_request_token(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Sync Request`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Sync Request 🚀](<Sync Calls 🚀.md>)')


@register_hardcoded("wallets", replacement=WALLETS_REPLACEMENT, token_label="Wallets")
def replace_wallets_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Wallets`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, WALLETS_REPLACEMENT)


@register_hardcoded("wallet", replacement=WALLET_REPLACEMENT, token_label="Wallet")
def replace_wallet_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Wallet`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, WALLET_REPLACEMENT)


def replace_issuer_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Issuer`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    replacement = "[Issuer 🎴 domain](<🎴🎭 Issuer role.md>)"
    return _replace_simple(md_files, pattern, replacement)


def replace_issuers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Issuers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    replacement = "[Issuer 🎴 domains](<🎴🎭 Issuer role.md>)"
    return _replace_simple(md_files, pattern, replacement)


@register_hardcoded("vaults", replacement="[Vault 🗄️ domains](<🗄️🎭 Vault role.md>)", token_label="Vaults")
def replace_vaults_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Vaults`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    replacement = "[Vault 🗄️ domains](<🗄️🎭 Vault role.md>)"
    return _replace_simple(md_files, pattern, replacement)


@register_hardcoded("vault", replacement="[Vault 🗄️ domain](<🗄️🎭 Vault role.md>)", token_label="Vault")
def replace_vault_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Vault`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    replacement = "[Vault 🗄️ domain](<🗄️🎭 Vault role.md>)"
    return _replace_simple(md_files, pattern, replacement)


# Hardcoded Agent token
AGENT_REPLACEMENT = "[Agent 🫥 vault](<🫥🗄️ Agent vault.md>)"
@register_hardcoded("agent", replacement=AGENT_REPLACEMENT, token_label="Agent")
def replace_agent_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Agent`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, AGENT_REPLACEMENT)


# Hardcoded Prompt(s) tokens
PROMPT_REPLACEMENT = "[Prompt 🤔](<🤔 Prompt.md>)"
@register_hardcoded("prompt", replacement=PROMPT_REPLACEMENT, token_label="Prompt")
def replace_prompt_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Prompt`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, PROMPT_REPLACEMENT)


@register_hardcoded("prompts", replacement='[Prompts 🤔](<🤔 Prompt.md>)', token_label="Prompts")
def replace_prompts_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Prompts`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Prompts 🤔](<🤔 Prompt.md>)')


# Hardcoded Reviewer tokens
REVIEWER_REPLACEMENT = "[Reviewer ⭐ agent](<⭐ Reviewer 🫥 agent.md>)"
@register_hardcoded("reviewer", replacement=REVIEWER_REPLACEMENT, token_label="Reviewer")
def replace_reviewer_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Reviewer`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, REVIEWER_REPLACEMENT)


@register_hardcoded("reviewers", replacement='[Reviewer ⭐ agents](<⭐ Reviewer 🫥 agent.md>)', token_label="Reviewers")
def replace_reviewers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Reviewers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Reviewer ⭐ agents](<⭐ Reviewer 🫥 agent.md>)')


# Hardcoded Printer tokens
PRINTER_REPLACEMENT = "[Printer 🖨️ helper](<🖨️🤲 Printer helper.md>)"


@register_hardcoded("printer", replacement=PRINTER_REPLACEMENT, token_label="Printer")
def replace_printer_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Printer`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, PRINTER_REPLACEMENT)


@register_hardcoded("printers", replacement='[Printer 🖨️ helpers](<🖨️🤲 Printer helper.md>)', token_label="Printers")
def replace_printers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Printers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Printer 🖨️ helpers](<🖨️🤲 Printer helper.md>)')


# Hardcoded Authority tokens
AUTHORITY_REPLACEMENT = "[Authority 🏛️ domain](<🏛️🤲 Authority helper.md>)"


@register_hardcoded("authority", replacement=AUTHORITY_REPLACEMENT, token_label="Authority")
def replace_authority_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Authority`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, AUTHORITY_REPLACEMENT)


@register_hardcoded("authorities", replacement='[Authority 🏛️ domains](<🏛️🤲 Authority helper.md>)', token_label="Authorities")
def replace_authorities_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Authorities`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Authority 🏛️ domains](<🏛️🤲 Authority helper.md>)')


# Hardcoded Map token with case-sensitive link text handling
_MAP_PATTERN = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Mm]ap)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")


@register_hardcoded("map", replacement="[Map 🧠 holder](<🧠 Map holders.md>)|[map](<🧠 Map holders.md>)", token_label="Map")
def replace_map_tokens(md_files):
    total = 0
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            # Emit lowercase variant without the emoji when the token is fully lowercase
            replacement = "[map](<🧠 Map holders.md>)" if token_value.islower() else "[Map 🧠 holder](<🧠 Map holders.md>)"
            changes += 1
            return replacement

        new_content = _MAP_PATTERN.sub(_repl, content)

        if changes:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += changes

    return total


@register_hardcoded("bool", replacement="[Bool 🧠 holder](<Bool holders.md>)|[bool](<Bool holders.md>)", token_label="Bool")
def replace_bool_tokens(md_files):
    """Replace {{Bool}}/{{bool}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Bb]ool)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[bool](<Bool holders.md>)" if token_value.islower() else "[Bool 🧠 holder](<Bool holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded("list", replacement="[List 🧠 holder](<🧠 List holders.md>)|[list](<🧠 List holders.md>)", token_label="List")
def replace_list_tokens(md_files):
    """Replace {{List}}/{{list}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Ll]ist)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[list](<🧠 List holders.md>)" if token_value.islower() else "[List 🧠 holder](<🧠 List holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded("text", replacement="[Text 🧠 holder](<🧠 Text holders.md>)|[text](<🧠 Text holders.md>)", token_label="Text")
def replace_text_tokens(md_files):
    """Replace {{Text}}/{{text}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Tt]ext)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[text](<🧠 Text holders.md>)" if token_value.islower() else "[Text 🧠 holder](<🧠 Text holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded("set", replacement="[Set 🧠 holder](<🧠 Set holders.md>)|[set](<🧠 Set holders.md>)", token_label="Set")
def replace_set_tokens(md_files):
    """Replace {{Set}}/{{set}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Ss]et)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[set](<🧠 Set holders.md>)" if token_value.islower() else "[Set 🧠 holder](<🧠 Set holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded("num", replacement="[Num 🧠 holder](<🧠 Num holders.md>)|[num](<🧠 Num holders.md>)", token_label="Num")
def replace_num_tokens(md_files):
    """Replace {{Num}}/{{num}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Nn]um)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[num](<🧠 Num holders.md>)" if token_value.islower() else "[Num 🧠 holder](<🧠 Num holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded("time", replacement="[Time 🧠 holder](<🧠 Time holders.md>)|[time](<🧠 Time holders.md>)", token_label="Time")
def replace_time_tokens(md_files):
    """Replace {{Time}}/{{time}} tokens while preserving link text casing."""

    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?([Tt]ime)`?[\s\u00A0\u200B\u200C\u200D]*\}\}")
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)
    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        link_spans = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in link_spans)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_value = match.group(1)
            replacement = "[time](<🧠 Time holders.md>)" if token_value.islower() else "[Time 🧠 holder](<🧠 Time holders.md>)"
            changes += 1
            return replacement

        new_content, count = pattern.subn(_repl, content)

        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


@register_hardcoded("maps", replacement='[Map 🧠 holders](<🧠 Map holders.md>)', token_label="Maps")
def replace_maps_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Maps`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Map 🧠 holders](<🧠 Map holders.md>)')


# Generate common simple replacers to reduce repeated boilerplate. These are
# intentionally created via helper to keep the explicit simple cases compact.
_GEN_BASIC = [
    ("replace_token_tokens", "Token", "token", "[Token 🎫](<🎫 Token.md>)", "Token"),
    ("replace_tokens_tokens", "Tokens", "tokens", "[Tokens 🎫](<🎫 Token.md>)", "Tokens"),
    ("replace_bools_tokens", "Bools", "bools", "[Bool 🧠 holders](<Bool holders.md>)", "Bools"),
    ("replace_chat_tokens", "Chat", "chat", "[Chat 💬](<💬 Chat.md>)", "Chat"),
    ("replace_chats_tokens", "Chats", "chats", "[Chats 💬](<💬 Chat.md>)", "Chats"),
    ("replace_settings_tokens", "$.Hosted", "$.settings", "[`$.Hosted` 🧠 holder](<📦 $.Hosted 🧠 holder.md>)", "$.Hosted"),
    ("replace_placeholders_tokens", "Placeholders", "placeholders", "[Placeholders 🧠](<Holder 🧠.md>)", "Placeholders"),
    ("replace_lists_tokens", "Lists", "lists", "[List 🧠 holders](<🧠 List holders.md>)", "Lists"),
    ("replace_sets_tokens", "Sets", "sets", "[Set 🧠 holders](<🧠 Set holders.md>)", "Sets"),
    ("replace_nums_tokens", "Nums", "nums", "[Num 🧠 holders](<🧠 Num holders.md>)", "Nums"),
    ("replace_bind_tokens", "Bind", "bind", "[Bind 🔗](<🔗 Bind.md>)", "Bind"),
    ("replace_binds_tokens", "Binds", "binds", "[Binds 🔗](<🔗 Bind.md>)", "Binds"),
    ("replace_locator_tokens", "Locator", "locator", "[Locator 🔆](<🔆 Locator.md>)", "Locator"),
    ("replace_locators_tokens", "Locators", "locators", "[Locators 🔆](<🔆 Locator.md>)", "Locators"),
    ("replace_texts_tokens", "Texts", "texts", "[Text 🧠 holders](<🧠 Text holders.md>)", "Texts"),
    ("replace_domain_tokens", "domain", "domain", "[domain 👥](<👥 Domain.md>)", "domain"),
    ("replace_domains_tokens", "domains", "domains", "[domains 👥](<👥 Domain.md>)", "domains"),
    ("replace_dataset_tokens", "Dataset", "dataset", "[Dataset 🪣](<🪣 Dataset.md>)", "Dataset"),
    ("replace_datasets_tokens", "Datasets", "datasets", "[Datasets 🪣](<🪣 Dataset.md>)", "Datasets"),
    ("replace_message_tokens", "Message", "message", "[Message 📨](<📨 Message.md>)", "Message"),
    ("replace_messages_tokens", "Messages", "messages", "[Messages 📨](<📨 Message.md>)", "Messages"),
    ("replace_schema_tokens", "Schema", "schema", "[Schema Code 🧩](<🧩 Schema Code.md>)", "Schema"),
    ("replace_schemas_tokens", "Schemas", "schemas", "[Schema Codes 🧩](<🧩 Schema Code.md>)", "Schemas"),
    ("replace_chat_msg_tokens", "$.Chat", "$.chat", "[`$.Chat` 🧠 holder](<💬 $.Chat 🧠 holder.md>)", "$.Chat"),
    ("replace_times_tokens", "Times", "times", "[Time 🧠 holders](<🧠 Time holders.md>)", "Times"),
    ("replace_period_tokens", "Period", "period", "[Period 🧠 holder](<Period holders.md>)", "Period"),
    ("replace_periods_tokens", "Periods", "periods", "[Period 🧠 holders](<Period holders.md>)", "Periods"),
    ("replace_nums_tokens", "Nums", "nums", "[Num 🧠 holders](<🧠 Num holders.md>)", "Nums"),
    ("replace_command_tokens", "Command", "command", COMMAND_REPLACEMENT, "Command"),
    ("replace_commands_tokens", "Commands", "commands", COMMANDS_REPLACEMENT, "Commands"),
    ("replace_script_tokens", "Script", "script", SCRIPT_REPLACEMENT, "Script"),
    ("replace_manifest_tokens", "Manifest", "manifest", MANIFEST_REPLACEMENT, "Manifest"),
    ("replace_manifests_tokens", "Manifests", "manifests", MANIFESTS_REPLACEMENT, "Manifests"),
    ("replace_persona_tokens", "Persona", "persona", "[Persona 🧢 agent](<🧢🫥 Persona agent.md>)", "Persona"),
    ("replace_personas_tokens", "Personas", "personas", "[Persona 🧢 agents](<🧢🫥 Persona agent.md>)", "Personas"),
    ("replace_itemizer_tokens", "Itemizer", "itemizer", "[Itemizer 🛢 helper domain](<🛢🤲 Itemizer helper.md>)", "Itemizer"),
    ("replace_itemizers_tokens", "Itemizers", "itemizers", "[Itemizer 🛢 helper domains](<🛢🤲 Itemizer helper.md>)", "Itemizers"),
]

for fname, lit, key, repl, label in _GEN_BASIC:
    _make_hardcoded_replacer(fname, lit, key, repl, label)


@register_hardcoded("broker", replacement=BROKER_REPLACEMENT, token_label="Broker")
def replace_broker_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Broker`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, BROKER_REPLACEMENT)


@register_hardcoded("biller", replacement=BILLER_REPLACEMENT, token_label="Biller")
def replace_biller_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Biller`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, BILLER_REPLACEMENT)


@register_hardcoded("billers", replacement=BILLERS_REPLACEMENT, token_label="Billers")
def replace_billers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Billers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, BILLERS_REPLACEMENT)


@register_hardcoded("seller", replacement=SELLER_REPLACEMENT, token_label="Seller")
def replace_seller_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Seller`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, SELLER_REPLACEMENT)


@register_hardcoded("sellers", replacement=SELLERS_REPLACEMENT, token_label="Sellers")
def replace_sellers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Sellers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, SELLERS_REPLACEMENT)


@register_hardcoded("streamer", replacement=STREAMER_REPLACEMENT, token_label="Streamer")
def replace_streamer_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Streamer`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, STREAMER_REPLACEMENT)


@register_hardcoded("streamers", replacement=STREAMERS_REPLACEMENT, token_label="Streamers")
def replace_streamers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Streamers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, STREAMERS_REPLACEMENT)


@register_hardcoded("graph", replacement=GRAPH_REPLACEMENT, token_label="Graph")
def replace_graph_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Graph`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, GRAPH_REPLACEMENT)


@register_hardcoded("graphs", replacement=GRAPHS_REPLACEMENT, token_label="Graphs")
def replace_graphs_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Graphs`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, GRAPHS_REPLACEMENT)


@register_hardcoded("subscriber", replacement=SUBSCRIBER_REPLACEMENT, token_label="Subscriber")
def replace_subscriber_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Subscriber`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, SUBSCRIBER_REPLACEMENT)


@register_hardcoded("subscribers", replacement=SUBSCRIBERS_REPLACEMENT, token_label="Subscribers")
def replace_subscribers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Subscribers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, SUBSCRIBERS_REPLACEMENT)


# Hardcoded Logger tokens
LOGGER_REPLACEMENT = "[Logger 🪵 helper domain](<🪵 Logger 🤲 helper.md>)"
@register_hardcoded("logger", replacement=LOGGER_REPLACEMENT, token_label="Logger")
def replace_logger_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Logger`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, LOGGER_REPLACEMENT)


@register_hardcoded("loggers", replacement='[Logger 🪵 helper domains](<🪵 Logger 🤲 helper.md>)', token_label="Loggers")
def replace_loggers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Loggers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Logger 🪵 helper domains](<🪵 Logger 🤲 helper.md>)')


@register_hardcoded("consumer", replacement=CONSUMER_REPLACEMENT, token_label="Consumer")
def replace_consumer_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Consumer`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, CONSUMER_REPLACEMENT)


@register_hardcoded("consumers", replacement=CONSUMERS_REPLACEMENT, token_label="Consumers")
def replace_consumers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Consumers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, CONSUMERS_REPLACEMENT)


@register_hardcoded("brokers", replacement='[Broker 🤵 domains](<🤵 Broker 🤲 helper.md>)', token_label="Brokers")
def replace_brokers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Brokers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Broker 🤵 domains](<🤵 Broker 🤲 helper.md>)")


def replace_function_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Function`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    # Link text shows the function placeholder with braces, but the target file
    # is named without braces (e.g. "Function 🐍.md"). Keep link text as-is
    # but point to the correct existing file.
    return _replace_simple(md_files, pattern, "[{Function} 🐍](<Function 🐍.md>)")


def replace_functions_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Functions`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    # Similar to single-function case; target file is "Function 🐍.md"
    return _replace_simple(md_files, pattern, "[{Functions} 🐍](<Function 🐍.md>)")


def replace_dot_function_tokens(md_files: Iterable[str]) -> int:
    """Replace tokens like ``{{.UUID}}`` with links to their ⓕ function docs."""

    function_index = _build_dot_function_index(md_files)
    if not function_index:
        return 0

    total = 0

    for md_file in md_files:
        path = Path(md_file)
        entry = _get_cached_entry(path)
        if not entry:
            continue

        content = entry["content"]
        if "{{." not in content:
            continue

        link_spans = entry.get("link_spans")
        if link_spans is None:
            spans = [m.span() for m in LINK_PATTERN.finditer(content)]
            entry["link_spans"] = spans
            link_spans = spans

        spans_tuple = tuple(link_spans)

        def inside_link(pos: int) -> bool:
            return any(a <= pos < b for a, b in spans_tuple)

        changes = 0

        def _repl(match: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(match.start()):
                return match.group(0)

            token_name = match.group(1)
            normalized_token = normalize_string(token_name)
            target_path = function_index.get(normalized_token)
            if not target_path:
                return match.group(0)

            try:
                rel_path = os.path.relpath(target_path, path.parent)
            except Exception:
                rel_path = target_path.name

            changes += 1
            return f"[`.{token_name}`](<{rel_path}>)"

        new_content = _DOT_FUNCTION_PATTERN.sub(_repl, content)
        if not changes:
            continue

        try:
            path.write_text(new_content, encoding="utf-8")
        except Exception:
            continue

        entry["content"] = new_content
        entry["link_spans"] = None
        entry["lower"] = None
        total += changes

    return total


@register_hardcoded("scripts", replacement=SCRIPTS_REPLACEMENT, token_label="Scripts")
def replace_scripts_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Scripts`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, SCRIPTS_REPLACEMENT)


def replace_item_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Item`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Item 🛢](<Itemized 🛢 dataset.md>)")


def replace_items_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Items`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[`Items` 🛢](<Itemized 🛢 dataset.md>)")


def replace_itemizer_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemizer`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    replacement = "[Itemizer 🛢 helper domain](<../../🛢🤲 Itemizer helper.md>)"
    return _replace_simple(md_files, pattern, replacement)


def replace_itemizers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemizers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    replacement = "[Itemizer 🛢 helper domains](<../../🛢🤲 Itemizer helper.md>)"
    return _replace_simple(md_files, pattern, replacement)


def replace_talker_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Talker`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Talker 😃 domain](<😃 Talker role.md>)")


def replace_talkers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Talkers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Talker 😃 domains](<😃 Talker role.md>)")


@register_hardcoded(
    "itemizeddataset",
    replacement="[Itemized 🪣 dataset](<Itemized 🛢 dataset.md>)",
    token_label="Itemized dataset",
)
def replace_itemized_dataset_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemized dataset`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Itemized 🪣 dataset](<Itemized 🛢 dataset.md>)")


def replace_itemized_datasets_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemized datasets`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Itemized 🪣 datasets](<Itemized 🛢 dataset.md>)")


@register_hardcoded("notifier", replacement="[Notifier 📣 domain](<📣 Notifier 👥 domain.md>)", token_label="Notifier")
def replace_notifier_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Notifier`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Notifier 📣 domain](<📣 Notifier 👥 domain.md>)")


@register_hardcoded("notifiers", replacement="[Notifier 📣 domains](<📣 Notifier 👥 domain.md>)", token_label="Notifiers")
def replace_notifiers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Notifiers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Notifier 📣 domains](<📣 Notifier 👥 domain.md>)")


def replace_triple_brace_tokens(md_files: Iterable[str], file_dict: dict[str, list[tuple[str, str]]]) -> int:
    """Replace helper tokens using triple braces with markdown links."""

    total = 0

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        def replacer(match: re.Match[str]) -> str:
            token = match.group(1).strip()
            target = find_dynamic_target(token, file_dict)
            if not target:
                return match.group(0)

            try:
                rel_path = os.path.relpath(target, path.parent)
            except Exception:
                rel_path = str(target)

            link_text = format_dynamic_link_text(token, triple_brace=True)
            return f"[{link_text}](<{rel_path}>)"

        new_content, count = TRIPLE_BRACE_PATTERN.subn(replacer, content)
        if count:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += count

    return total


__all__ = [
    "HARDCODED_HANDLERS",
    "replace_placeholder_tokens",
    "replace_msg_tokens",
    "replace_hosts_tokens",
    "replace_host_tokens",
    "replace_issuer_tokens",
    "replace_issuers_tokens",
    "replace_vaults_tokens",
    "replace_vault_tokens",
    "replace_wallet_tokens",
    "replace_wallets_tokens",
    "replace_token_tokens",
    "replace_triple_brace_tokens",
    "replace_tokens_tokens",
    "replace_script_tokens",
    "replace_manifest_tokens",
    "replace_manifests_tokens",
    "replace_chat_tokens",
    "replace_chats_tokens",
    "replace_command_tokens",
    "replace_commands_tokens",
    "replace_settings_tokens",
    "replace_placeholders_tokens",
    "replace_domain_tokens",
    "replace_domains_tokens",
    "replace_dataset_tokens",
    "replace_datasets_tokens",
    "replace_set_tokens",
    "replace_sets_tokens",
    "replace_period_tokens",
    "replace_periods_tokens",
    "replace_num_tokens",
    "replace_nums_tokens",
    "replace_message_tokens",
    "replace_messages_tokens",
    "replace_schema_tokens",
    "replace_schemas_tokens",
    "replace_chat_msg_tokens",
    "replace_broker_tokens",
    "replace_brokers_tokens",
    "replace_seller_tokens",
    "replace_sellers_tokens",
    "replace_subscriber_tokens",
    "replace_subscribers_tokens",
    "replace_streamer_tokens",
    "replace_streamers_tokens",
    "replace_graph_tokens",
    "replace_graphs_tokens",
    "replace_function_tokens",
    "replace_functions_tokens",
    "replace_dot_function_tokens",
    "replace_scripts_tokens",
    "replace_item_tokens",
    "replace_items_tokens",
    "replace_itemizer_tokens",
    "replace_itemizers_tokens",
    "replace_talker_tokens",
    "replace_talkers_tokens",
    "replace_itemized_dataset_tokens",
    "replace_itemized_datasets_tokens",
    "replace_notifier_tokens",
    "replace_notifiers_tokens",
]
