"""Straightforward token replacement helpers."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Callable, Dict, Iterable

from broken_links.common import normalize_string
from .mentions import find_dynamic_target, format_dynamic_link_text


HARDCODED_HANDLERS: Dict[str, Dict[str, object]] = {}
TRIPLE_BRACE_PATTERN = re.compile(r"\{\{\{([^{}]+)\}\}\}")


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


def _replace_simple(md_files: Iterable[str], pattern: re.Pattern[str], replacement: str) -> int:
    """Replace occurrences of pattern with replacement, but skip matches
    that are already inside existing markdown links (e.g. [text](<...>)).

    This prevents nested or malformed links when multiple replacement
    passes run over the same files.
    """
    total = 0
    link_pattern = re.compile(r"\[.*?\]\(<.*?>\)", re.DOTALL)

    for md_file in md_files:
        path = Path(md_file)
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue

        # collect spans of existing markdown links so we can skip matches
        link_spans: list[tuple[int, int]] = [m.span() for m in link_pattern.finditer(content)]

        def inside_link(pos: int) -> bool:
            for a, b in link_spans:
                if a <= pos < b:
                    return True
            return False

        changes = 0

        def _repl(m: re.Match[str]) -> str:
            nonlocal changes
            if inside_link(m.start()):
                return m.group(0)
            changes += 1
            return replacement

        new_content = pattern.sub(_repl, content)

        if changes:
            try:
                path.write_text(new_content, encoding="utf-8")
            except Exception:
                continue
            total += changes

    return total


def _simple_pattern_for(token_literal: str) -> re.Pattern[str]:
    """Build a simple regex pattern matching {{ `Token` }} variants for a token literal."""

    pattern = rf"\{{\{{[\s\u00A0\u200B\u200C\u200D]*`?{re.escape(token_literal)}`?[\s\u00A0\u200B\u200C\u200D]*\}}\}}"
    return re.compile(pattern, re.IGNORECASE)


def _make_hardcoded_replacer(func_name: str, token_literal: str, token_key: str, replacement: str, token_label: str):
    """Dynamically create and register a simple hardcoded replacer.

    The created function will be available in module globals under `func_name`
    and also registered in HARDCODED_HANDLERS under `token_key`.
    """

    pattern = _simple_pattern_for(token_literal)

    def replacer(md_files: Iterable[str]) -> int:
        return _replace_simple(md_files, pattern, replacement)

    replacer.__name__ = func_name
    globals()[func_name] = replacer
    HARDCODED_HANDLERS[token_key] = {"func": replacer, "replacement": replacement, "token_label": token_label}
    return replacer


PLACEHOLDER_REPLACEMENT = "[Placeholder 🧠](<$Placeholder 🧠.md>)"
HOLDER_REPLACEMENT = "[Holder 🧠](<Holder 🧠.md>)"
HOSTS_REPLACEMENT = "[Host 🤗 domains](<../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)"
HOST_REPLACEMENT = "[Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)"
SCRIPT_REPLACEMENT = "[Script 📃](<Script 📃.md>)"
SCRIPTS_REPLACEMENT = "[Scripts 📃](<Script 📃.md>)"
COMMAND_REPLACEMENT = "[Command ⌘](<⌘ Command.md>)"
COMMANDS_REPLACEMENT = "[Commands ⌘](<⌘ Command.md>)"
BROKER_REPLACEMENT = "[Broker 🤵 domain](<🤵🤲 Broker helper.md>)"
SELLER_REPLACEMENT = "[Seller 🎭 domain](<../../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>)"
CONSUMER_REPLACEMENT = "[Consumer 💼 domain](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>)"
CONSUMERS_REPLACEMENT = "[Consumer 💼 domains](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>)"
WALLET_REPLACEMENT = "[Wallet 🧑‍🦰 app](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)"
WALLETS_REPLACEMENT = "[Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)"


@register_hardcoded("placeholder", replacement=PLACEHOLDER_REPLACEMENT, token_label="Placeholder")
def replace_placeholder_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Placeholder`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, PLACEHOLDER_REPLACEMENT)


@register_hardcoded("holder", replacement=HOLDER_REPLACEMENT, token_label="Holder")
def replace_holder_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Holder`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, HOLDER_REPLACEMENT)


def replace_msg_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?\$\.Msg`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    # Use the holder file for $.Msg (emoji then token then '🧠 holder')
    replacement = "[`$.Msg` 🧠 holder](<📨 $.Msg 🧠 holder.md>)"
    return _replace_simple(md_files, pattern, replacement)


@register_hardcoded("hosts", replacement=HOSTS_REPLACEMENT, token_label="Hosts")
def replace_hosts_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Hosts`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, HOSTS_REPLACEMENT)


@register_hardcoded("host", replacement=HOST_REPLACEMENT, token_label="Host")
def replace_host_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Host`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, HOST_REPLACEMENT)


@register_hardcoded("hosted", replacement='[Hosted 📦 domain](<📦👥 Hosted domain.md>)', token_label="Hosted")
def replace_hosted_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Hosted`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Hosted 📦 domain](<📦👥 Hosted domain.md>)')


@register_hardcoded("hosteds", replacement='[Hosted 📦 domains](<📦👥 Hosted domain.md>)', token_label="Hosteds")
def replace_hosteds_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Hosteds`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Hosted 📦 domains](<📦👥 Hosted domain.md>)')


# Hardcoded Trust token
TRUST_REPLACEMENT = "[Trust 🫡](<🫡 Domain Trust.md>)"
@register_hardcoded("trust", replacement=TRUST_REPLACEMENT, token_label="Trust")
def replace_trust_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Trust`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, TRUST_REPLACEMENT)


@register_hardcoded("trusted", replacement='[Trusted 🫡](<🫡 Domain Trust.md>)', token_label="Trusted")
def replace_trusted_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Trusted`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Trusted 🫡](<🫡 Domain Trust.md>)')


@register_hardcoded("holders", replacement='[Holders 🧠](<$Holder 🧠.md>)', token_label="Holders")
def replace_holders_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Holders`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Holders 🧠](<Holder 🧠.md>)')


# Hardcoded Helper token
HELPER_REPLACEMENT = "[Helper 🤲 domain](<🤲👥 Helper domain.md>)"
@register_hardcoded("helper", replacement=HELPER_REPLACEMENT, token_label="Helper")
def replace_helper_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Helper`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, HELPER_REPLACEMENT)


@register_hardcoded("helpers", replacement='[Helper 🤲 domains](<🤲👥 Helper domain.md>)', token_label="Helpers")
def replace_helpers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Helpers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Helper 🤲 domains](<🤲👥 Helper domain.md>)')


# Hardcoded Hoster tokens
HOSTER_REPLACEMENT = "[Hoster ☁️ helper domain](<☁️🤲 Hoster helper.md>)"
@register_hardcoded("hoster", replacement=HOSTER_REPLACEMENT, token_label="Hoster")
def replace_hoster_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Hoster`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, HOSTER_REPLACEMENT)


@register_hardcoded("hosters", replacement='[Hoster ☁️ helper domains](<☁️🤲 Hoster helper.md>)', token_label="Hosters")
def replace_hosters_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Hosters`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Hoster ☁️ helper domains](<☁️🤲 Hoster helper.md>)')


# Hardcoded Talker tokens
TALKER_REPLACEMENT = "[Talker 😃 helper domain](<😃🤲 Talker helper.md>)"
@register_hardcoded("talker", replacement=TALKER_REPLACEMENT, token_label="Talker")
def replace_talker_helper_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Talker`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, TALKER_REPLACEMENT)


@register_hardcoded("talkers", replacement='[Talker 😃 helper domains](<😃🤲 Talker helper.md>)', token_label="Talkers")
def replace_talkers_helper_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Talkers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Talker 😃 helper domains](<😃🤲 Talker helper.md>)')


# Hardcoded Role token
ROLE_REPLACEMENT = "[Role 🎭](<👥🎭 Domain Role.md>)"
@register_hardcoded("role", replacement=ROLE_REPLACEMENT, token_label="Role")
def replace_role_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Role`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, ROLE_REPLACEMENT)


@register_hardcoded("roles", replacement='[Roles 🎭](<👥🎭 Domain Role.md>)', token_label="Roles")
def replace_roles_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Roles`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Roles 🎭](<👥🎭 Domain Role.md>)')


# Hardcoded Async Message(s) tokens
ASYNC_MESSAGES_REPLACEMENT = "[Async Messages 🐌](<Async Messages 🐌.md>)"
@register_hardcoded("asyncmessages", replacement=ASYNC_MESSAGES_REPLACEMENT, token_label="Async Messages")
def replace_async_messages_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Async Messages`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, ASYNC_MESSAGES_REPLACEMENT)


@register_hardcoded("asyncmessage", replacement='[Async Message 🐌](<Async Messages 🐌.md>)', token_label="Async Message")
def replace_async_message_token(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Async Message`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Async Message 🐌](<Async Messages 🐌.md>)')


# Hardcoded Sync Request(s) tokens
SYNC_REQUESTS_REPLACEMENT = "[Sync Requests 🚀](<Sync Requests 🚀.md>)"
@register_hardcoded("syncrequests", replacement=SYNC_REQUESTS_REPLACEMENT, token_label="Sync Requests")
def replace_sync_requests_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Sync Requests`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, SYNC_REQUESTS_REPLACEMENT)


@register_hardcoded("syncrequest", replacement='[Sync Request 🚀](<Sync Requests 🚀.md>)', token_label="Sync Request")
def replace_sync_request_token(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Sync Request`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, '[Sync Request 🚀](<Sync Requests 🚀.md>)')


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
    replacement = "[Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)"
    return _replace_simple(md_files, pattern, replacement)


def replace_issuers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Issuers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    replacement = "[Issuer 🎴 domains](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)"
    return _replace_simple(md_files, pattern, replacement)


@register_hardcoded("vaults", replacement="[Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)", token_label="Vaults")
def replace_vaults_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Vaults`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    replacement = "[Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)"
    return _replace_simple(md_files, pattern, replacement)


@register_hardcoded("vault", replacement="[Vault 🗄️ domain](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)", token_label="Vault")
def replace_vault_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Vault`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    replacement = "[Vault 🗄️ domain](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)"
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
# Generate common simple replacers to reduce repeated boilerplate. These are
# intentionally created via helper to keep the explicit simple cases compact.
_GEN_BASIC = [
    ("replace_token_tokens", "Token", "token", "[Token 🎫](<🎫 Token.md>)", "Token"),
    ("replace_tokens_tokens", "Tokens", "tokens", "[Tokens 🎫](<🎫 Token.md>)", "Tokens"),
    ("replace_chat_tokens", "Chat", "chat", "[Chat 💬](<💬 Chat.md>)", "Chat"),
    ("replace_chats_tokens", "Chats", "chats", "[Chats 💬](<💬 Chat.md>)", "Chats"),
    ("replace_settings_tokens", "$.Hosted", "$.settings", "[`$.Hosted` 🧠 holder](<📦 $.Hosted 🧠 holder.md>)", "$.Hosted"),
    ("replace_placeholders_tokens", "Placeholders", "placeholders", "[Placeholders 🧠](<$Placeholder 🧠.md>)", "Placeholders"),
    ("replace_domain_tokens", "domain", "domain", "[domain 👥](<👥 Domain.md>)", "domain"),
    ("replace_domains_tokens", "domains", "domains", "[domains 👥](<👥 Domain.md>)", "domains"),
    ("replace_dataset_tokens", "Dataset", "dataset", "[Dataset 🪣](<🪣 Dataset.md>)", "Dataset"),
    ("replace_datasets_tokens", "Datasets", "datasets", "[Datasets 🪣](<🪣 Dataset.md>)", "Datasets"),
    ("replace_message_tokens", "Message", "message", "[Message 📨](<📨 Message.md>)", "Message"),
    ("replace_messages_tokens", "Messages", "messages", "[Messages 📨](<📨 Message.md>)", "Messages"),
    ("replace_schema_tokens", "Schema", "schema", "[Schema Code 🧩](<🧩 Schema Code.md>)", "Schema"),
    ("replace_schemas_tokens", "Schemas", "schemas", "[Schema Codes 🧩](<🧩 Schema Code.md>)", "Schemas"),
    ("replace_chat_msg_tokens", "$.Chat", "$.chat", "[`$.Chat` 🧠 holder](<💬 $.Chat 🧠 holder.md>)", "$.Chat"),
    ("replace_command_tokens", "Command", "command", COMMAND_REPLACEMENT, "Command"),
    ("replace_commands_tokens", "Commands", "commands", COMMANDS_REPLACEMENT, "Commands"),
    ("replace_script_tokens", "Script", "script", SCRIPT_REPLACEMENT, "Script"),
]

for fname, lit, key, repl, label in _GEN_BASIC:
    _make_hardcoded_replacer(fname, lit, key, repl, label)


@register_hardcoded("broker", replacement=BROKER_REPLACEMENT, token_label="Broker")
def replace_broker_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Broker`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, BROKER_REPLACEMENT)


@register_hardcoded("seller", replacement=SELLER_REPLACEMENT, token_label="Seller")
def replace_seller_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Seller`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, SELLER_REPLACEMENT)


@register_hardcoded("consumer", replacement=CONSUMER_REPLACEMENT, token_label="Consumer")
def replace_consumer_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Consumer`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, CONSUMER_REPLACEMENT)


@register_hardcoded("consumers", replacement=CONSUMERS_REPLACEMENT, token_label="Consumers")
def replace_consumers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Consumers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, CONSUMERS_REPLACEMENT)


def replace_brokers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Brokers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Broker 🤵 domains](<🤵🤲 Broker helper.md>)")


def replace_function_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Function`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[{Function} 🐍](<{Function} 🐍.md>)")


def replace_functions_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Functions`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[{Functions} 🐍](<{Function} 🐍.md>)")


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


def replace_itemized_dataset_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemized dataset`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Itemized 🪣 dataset](<Itemized 🛢 dataset.md>)")


def replace_itemized_datasets_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemized datasets`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Itemized 🪣 datasets](<Itemized 🛢 dataset.md>)")


def replace_notifier_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Notifier`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Notifier 📣 domain](<📣👥 Notifier domain.md>)")


def replace_notifiers_tokens(md_files):
    pattern = re.compile(r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Notifiers`?[\s\u00A0\u200B\u200C\u200D]*\}\}", re.IGNORECASE)
    return _replace_simple(md_files, pattern, "[Notifier 📣 domains](<📣👥 Notifier domain.md>)")


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
    "replace_message_tokens",
    "replace_messages_tokens",
    "replace_schema_tokens",
    "replace_schemas_tokens",
    "replace_chat_msg_tokens",
    "replace_broker_tokens",
    "replace_brokers_tokens",
    "replace_seller_tokens",
    "replace_function_tokens",
    "replace_functions_tokens",
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
