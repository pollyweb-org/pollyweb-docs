import os
import re
import itertools
from collections import OrderedDict
import yaml

try:
    import emoji as _emoji_mod  # optional dependency
except Exception:
    _emoji_mod = None

# Globals used by worker processes (initialized via init_worker)
_EXISTING_FILES = None
_PROJECT_DIR = None

# Precompile regex patterns for performance
_LINK_WITH_TEXT_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(<?([^)>#]+)>?\)")
_LINK_WITH_TEXT_ANGLE_RE = re.compile(r"(?<!!)\[([^\]]+)\]<([^>#]+)>")
_ANGLE_AUTOLINK_RE = re.compile(r"(?<!!)<?<([^>#]+)>")

# Capture tokens like {{abc@def}} (any text with '@' inside double curly braces)
_CURLY_AT_TOKEN_RE = re.compile(r"\{\{([^{}]*@[^{}]*)\}\}")

# Match tokens like {{ABC}} where token is uppercase letters/digits/._-
_CURLY_UPPER_TOKEN_RE = re.compile(r"\{\{([A-Z][A-Z0-9._-]*)\}\}")

# Detect a table row that begins with a pipe followed by an uppercase token link
# Supports both forms: [`ABC`](<href>) and [`ABC`]<href>
_ROW_LEADING_UPPER_LINK_RE = re.compile(
    r"^\s*\|\s*"                                   # start of row and pipe
    r"\[`([A-Z][A-Z0-9._-]*)`\]"                    # link label in backticks
    r"(?:\(<?([^)>#]+)>?\)|<([^)>#]+)>)"            # either (...<href>...) or <href>
)

# Emoji detection: keycaps like 1️⃣, *️⃣, #️⃣ and general emoji/symbol blocks
_KEYCAP_EMOJI_RE = re.compile("(?:[0-9#*]\uFE0F?\u20E3)")
# Include a broad set: flags and emoji ranges, arrows, misc technical, geometric shapes (▶ U+25B6), misc symbols, dingbats, misc symbols & arrows
_GENERAL_EMOJI_RE = re.compile(
    "[\U0001F1E6-\U0001F1FF\U0001F300-\U0001FAFF\u2190-\u21FF\u2300-\u23FF\u25A0-\u25FF\u2600-\u26FF\u2700-\u27BF\u2B00-\u2BFF]\uFE0F?",
    re.UNICODE,
)

def normalize_string(s):
    # Remove emojis using regex (fallback if emoji library not available)
    s = _GENERAL_EMOJI_RE.sub('', s)
    # Remove spaces and lowercase
    ret = re.sub(r'\s+', '', s).lower()
    ret = ret.replace('$', '')
    return ret

def _extract_links_text_href(content):
    """Return list of (text, href) for markdown links in content (skip images and anchors)."""
    results = []
    seen = set()
    for text, href in _LINK_WITH_TEXT_RE.findall(content):
        key = (text, href)
        if key not in seen:
            seen.add(key)
            results.append((text, href))
    # Also support [`text`]<href> form
    for text, href in _LINK_WITH_TEXT_ANGLE_RE.findall(content):
        key = (text, href)
        if key not in seen:
            seen.add(key)
            results.append((text, href))
    return results

def _extract_curly_at_tokens(content):
    """Return list of unique tokens found inside {{...}} that contain '@'."""
    return list(dict.fromkeys(_CURLY_AT_TOKEN_RE.findall(content)))

def _pick_matching_link(token, links):
    """Pick a matching link from a list where each item is either (text, href) or (src, text, href).
    Returns a tuple (href, base_path) where base_path is the file the href is relative to (or None for same-file calls).
    """
    # Normalize for case-insensitive comparison backup
    token_lower = token.lower()

    # First pass: href contains token (case-sensitive)
    for item in links:
        if len(item) == 2:
            text, href = item
            base = None
        else:
            base, text, href = item
        if token in href:
            return href, base
    # Second pass: text contains token (case-sensitive)
    for item in links:
        if len(item) == 2:
            text, href = item
            base = None
        else:
            base, text, href = item
        if token in text:
            return href, base
    # Third pass: href contains token (case-insensitive)
    for item in links:
        if len(item) == 2:
            text, href = item
            base = None
        else:
            base, text, href = item
        if token_lower in href.lower():
            return href, base
    # Fourth pass: text contains token (case-insensitive)
    for item in links:
        if len(item) == 2:
            text, href = item
            base = None
        else:
            base, text, href = item
        if token_lower in text.lower():
            return href, base
    return None, None

def _pick_matching_link_upper(token, links):
    """Strict match for uppercase tokens: only accept links whose text is exactly `TOKEN`.
    Returns (href, base) or (None, None).
    """
    for item in links:
        if len(item) == 2:
            text, href = item
            base = None
        else:
            base, text, href = item
        t = text.strip()
        if len(t) >= 2 and t[0] == '`' and t[-1] == '`':
            inner = t[1:-1]
            if inner == token and inner.upper() == inner:
                return href, base
    return None, None

def _build_project_link_index(md_files):
    """Build a project-wide index of (source_path, text, href) from all md files."""
    index = []
    for path in md_files:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            for text, href in _extract_links_text_href(content):
                index.append((path, text, href))
            # Also include angle autolinks like <path/to/file.md>
            for href in _ANGLE_AUTOLINK_RE.findall(content):
                index.append((path, '', href))
        except Exception:
            continue
    return index

def replace_curly_at_mentions(md_files):
    """For each md file, replace {{token@other}} with [`token@other` 🅰️ method](<href>) if a matching file exists in the expected folder.

    Strategy: For token X@Y, find file *X*.md in folder containing *Y*methods*.
    """
    # Load failed tests
    yaml_path = os.path.join(os.path.dirname(__file__), 'links.yaml')
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    failed = {test['Given']: test.get('WrongFile') for test in data.get('Failed Tests', []) if 'WrongFile' in test}
    
    total_replacements = 0
    project_index = _build_project_link_index(md_files)

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue

        tokens = _extract_curly_at_tokens(content)
        if not tokens:
            continue

        links_here = _extract_links_text_href(content)
        changed = False

        for token in tokens:
            if '@' in token:
                parts = token.split('@', 1)
                X = parts[0]
                Y = parts[1]
                normalized_X = normalize_string(X)
                normalized_Y_methods = normalize_string(Y + 'methods')
                found_href = None
                for path in _EXISTING_FILES:
                    if normalize_string(os.path.basename(path)[:-3]) == normalized_X:
                        folder_path = os.path.dirname(path)
                        if normalized_Y_methods in normalize_string(folder_path):
                            found_href = os.path.relpath(path, os.path.dirname(md_file))
                            break
                if found_href:
                    # Check for wrong file
                    if token in failed and os.path.basename(found_href) == failed[token]:
                        raise ValueError(f"Generated wrong file link for {token}: {os.path.basename(found_href)}")
                    normalized = f"[`{token}` 🅰️ method](<{found_href}>)"
                    before = content
                    content = content.replace(f"{{{{{token}}}}}", normalized)
                    if content != before:
                        total_replacements += 1
                        changed = True

        if changed:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            except Exception:
                pass

    return total_replacements

def _extract_curly_upper_tokens(content):
    """Return list of unique uppercase tokens found inside {{...}} not containing '@'."""
    # This intentionally excludes tokens containing '@' (handled by the other feature)
    return list(dict.fromkeys(_CURLY_UPPER_TOKEN_RE.findall(content)))

def replace_curly_upper_mentions(md_files):
    """For each md file, replace {{TOKEN}} with [`TOKEN`](<href>) if a matching link exists.

    Strategy mirrors @-mentions: prefer same-file links; else project-wide; make href relative.
    """
    total_replacements = 0
    project_index = _build_project_link_index(md_files)

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue

        tokens = _extract_curly_upper_tokens(content)
        if not tokens:
            continue

        links_here = _extract_links_text_href(content)
        changed = False

        for token in tokens:
            # Strict: only pick links whose label is exactly `TOKEN`
            href, base = _pick_matching_link_upper(token, links_here)
            if not href:
                href, base = _pick_matching_link_upper(token, project_index)
            if not href and token.isupper():
                assumed_path = os.path.join(_PROJECT_DIR, "4 ⚙️ Solution", "35 💬 Chats", "😃 Talkers", "😃⚙️ Talker cmds", "for control", f"{token} ⤴️.md")
                if os.path.exists(assumed_path):
                    href = os.path.relpath(assumed_path, os.path.dirname(md_file))
                    base = None
            if not href:
                continue

            # If from another file, convert href relative to current file
            final_href = href
            try:
                if base and base != md_file and not href.startswith(('http://', 'https://', 'mailto:')):
                    abs_target = os.path.normpath(os.path.join(os.path.dirname(base), href))
                    final_href = os.path.relpath(abs_target, os.path.dirname(md_file))
            except Exception:
                final_href = href

            normalized = f"[`{token}`](<{final_href}>)"
            before = content
            content = content.replace(f"{{{{{token}}}}}", normalized)
            if content != before:
                total_replacements += 1
                changed = True

        if changed:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            except Exception:
                pass

    return total_replacements

def _find_first_emoji(text: str):
    """Return the first emoji sequence found in text, preferring keycaps, else general emoji."""
    m = _KEYCAP_EMOJI_RE.search(text)
    if m:
        return m.group(0)
    m = _GENERAL_EMOJI_RE.search(text)
    if m:
        return m.group(0)
    # Fallback using emoji library if available and regex failed
    if _emoji_mod:
        try:
            for ch in text:
                # Newer emoji libs expose EMOJI_DATA
                if hasattr(_emoji_mod, 'EMOJI_DATA') and ch in getattr(_emoji_mod, 'EMOJI_DATA'):
                    return ch
        except Exception:
            pass
    return None

def add_emoji_to_table_rows(md_files):
    """For rows starting with | [`UPPER`](<href>), take an emoji from the href's filename and prefix it."""
    import urllib.parse
    total_changes = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception:
            continue

        changed = False
        for i, line in enumerate(lines):
            m = _ROW_LEADING_UPPER_LINK_RE.match(line)
            if not m:
                continue

            # href captured either in group 2 (with parentheses) or group 3 (without)
            href = m.group(2) if m.group(2) is not None else m.group(3)
            # Skip external/anchors/mailto
            if href.startswith(('http://', 'https://', 'mailto:', '#')):
                continue

            # Decode and get filename
            href_decoded = urllib.parse.unquote(href)
            base = os.path.basename(href_decoded)
            emoji_char = _find_first_emoji(base)
            if not emoji_char:
                continue

            # If emoji already present immediately after the pipe, skip
            if re.match(r"^\s*\|\s*" + re.escape(emoji_char) + r"\s", line):
                continue

            # Insert emoji after first pipe
            new_line = re.sub(r"^(\s*\|\s*)", r"\g<1>" + emoji_char + " ", line, count=1)
            if new_line != line:
                lines[i] = new_line
                changed = True
                total_changes += 1

        if changed:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
            except Exception:
                pass

    return total_changes

# All the replace_*_tokens functions follow, each returning the number of replacements

def replace_placeholder_tokens(md_files):
    """Replace '{{Placeholder}}' (allowing optional inner spaces) with '[Placeholder 🧠](<$Placeholder 🧠.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Placeholder
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Placeholder`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Placeholder 🧠](<$Placeholder 🧠.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_msg_tokens(md_files):
    """Replace '{{$.Msg}}' (allowing optional inner spaces) with '[`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around $.Msg
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?\$\.Msg`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_hosts_tokens(md_files):
    """Replace '{{Hosts}}' (allowing optional inner spaces) with '[Host 🤗 domains](<../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Hosts
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Hosts`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Host 🤗 domains](<../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_host_tokens(md_files):
    """Replace '{{Host}}' (allowing optional inner spaces) with '[Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Host
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Host`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_issuer_tokens(md_files):
    """Replace '{{Issuer}}' (allowing optional inner spaces) with '[Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Issuer
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Issuer`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_issuers_tokens(md_files):
    """Replace '{{Issuers}}' (allowing optional inner spaces) with '[Issuer 🎴 domains](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Issuers
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Issuers`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Issuer 🎴 domains](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_vaults_tokens(md_files):
    """Replace '{{Vaults}}' (allowing optional inner spaces) with '[Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Vaults
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Vaults`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Vault 🗄️ domains](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_vault_tokens(md_files):
    """Replace '{{Vault}}' (allowing optional inner spaces) with '[Vault 🗄️ domain](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Vault
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Vault`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Vault 🗄️ domain](<../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_token_tokens(md_files):
    """Replace '{{Token}}' (allowing optional inner spaces) with '[Token 🎫](<🎫 Token.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Token
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Token`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Token 🎫](<🎫 Token.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_tokens_tokens(md_files):
    """Replace '{{Tokens}}' (allowing optional inner spaces) with '[Tokens 🎫](<🎫 Token.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Tokens
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Tokens`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Tokens 🎫](<🎫 Token.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_script_tokens(md_files):
    """Replace '{{Script}}' (allowing optional inner spaces) with '[Script 📃](<📃 Script.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Script
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Script`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Script 📃](<📃 Script.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_chat_tokens(md_files):
    """Replace '{{Chat}}' (allowing optional inner spaces) with '[Chat 💬](<💬 Chat.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Chat
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Chat`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Chat 💬](<💬 Chat.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_chats_tokens(md_files):
    """Replace '{{Chats}}' (allowing optional inner spaces) with '[Chats 💬](<💬 Chat.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Chats
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Chats`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Chats 💬](<💬 Chat.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_command_tokens(md_files):
    """Replace '{{Command}}' (allowing optional inner spaces) with '[Command ⌘](<⌘ Command.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Command
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Command`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Command ⌘](<⌘ Command.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_commands_tokens(md_files):
    """Replace '{{Commands}}' (allowing optional inner spaces) with '[Commands ⌘](<⌘ Command.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Commands
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Commands`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Commands ⌘](<⌘ Command.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            total += n
        except Exception:
            pass
    return total

def replace_settings_tokens(md_files):
    """Replace '{{$.Settings}}' (allowing optional inner spaces) with '[`$.Settings`](<$.Settings 🎛️.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around $.Settings
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?\$\.Settings`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[`$.Settings`](<$.Settings 🎛️.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_placeholders_tokens(md_files):
    """Replace '{{Placeholders}}' (allowing optional inner spaces) with '[Placeholders 🧠](<$Placeholder 🧠.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Placeholders
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Placeholders`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Placeholders 🧠](<$Placeholder 🧠.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_domain_tokens(md_files):
    """Replace '{{domain}}' (allowing optional inner spaces) with '[domain 👥](<👥 Domain.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around domain
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?domain`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[domain 👥](<👥 Domain.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_domains_tokens(md_files):
    """Replace '{{domains}}' (allowing optional inner spaces) with '[domains 👥](<👥 Domain.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around domains
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?domains`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[domains 👥](<👥 Domain.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_dataset_tokens(md_files):
    """Replace '{{Dataset}}' (allowing optional inner spaces) with '[Dataset 🪣](<🪣 Dataset.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Dataset
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Dataset`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Dataset 🪣](<🪣 Dataset.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_datasets_tokens(md_files):
    """Replace '{{Datasets}}' (allowing optional inner spaces) with '[Datasets 🪣](<🪣 Dataset.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Datasets
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Datasets`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Datasets 🪣](<🪣 Dataset.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_message_tokens(md_files):
    """Replace '{{Message}}' (allowing optional inner spaces) with '[Message 📨](<📨 Message.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Message
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Message`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Message 📨](<📨 Message.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_messages_tokens(md_files):
    """Replace '{{Messages}}' (allowing optional inner spaces) with '[Messages 📨](<📨 Message.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Messages
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Messages`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Messages 📨](<📨 Message.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_schema_tokens(md_files):
    """Replace '{{Schema}}' (allowing optional inner spaces) with '[Schema Code 🧩](<🧩 Schema Code.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Schema
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Schema`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Schema Code 🧩](<🧩 Schema Code.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_schemas_tokens(md_files):
    """Replace '{{Schemas}}' (allowing optional inner spaces) with '[Schema Codes 🧩](<🧩 Schema Code.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Schemas
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Schemas`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Schema Codes 🧩](<🧩 Schema Code.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_chat_msg_tokens(md_files):
    """Replace '{{$.Chat}}' (allowing optional inner spaces) with '[`$.Chat`](<$.Chat 💬.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around $.Chat
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?\$\.Chat`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[`$.Chat`](<$.Chat 💬.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_broker_tokens(md_files):
    """Replace '{{Broker}}' (allowing optional inner spaces) with '[Broker 🤵 domain](<🤵🤲 Broker helper.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Broker
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Broker`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Broker 🤵 domain](<🤵🤲 Broker helper.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_brokers_tokens(md_files):
    """Replace '{{Brokers}}' (allowing optional inner spaces) with '[Broker 🤵 domains](<🤵🤲 Broker helper.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Brokers
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Brokers`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Broker 🤵 domains](<🤵🤲 Broker helper.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_function_tokens(md_files):
    """Replace '{{Function}}' (allowing optional inner spaces) with '[{Function} 🐍](<{Function} 🐍.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Function
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Function`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[{Function} 🐍](<{Function} 🐍.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_functions_tokens(md_files):
    """Replace '{{Functions}}' (allowing optional inner spaces) with '[{Functions} 🐍](<{Function} 🐍.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Functions
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Functions`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[{Functions} 🐍](<{Function} 🐍.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_scripts_tokens(md_files):
    """Replace '{{Scripts}}' (allowing optional inner spaces) with '[Scripts 📃](<📃 Script.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Scripts
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Scripts`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Scripts 📃](<📃 Script.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_item_tokens(md_files):
    """Replace '{{Item}}' (allowing optional inner spaces) with '[Item 🛢](<Itemized 🛢 dataset.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Item
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Item`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Item 🛢](<Itemized 🛢 dataset.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_items_tokens(md_files):
    """Replace '{{Items}}' (allowing optional inner spaces) with '[`Items` 🛢](<Itemized 🛢 dataset.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Items
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Items`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[`Items` 🛢](<Itemized 🛢 dataset.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_itemizer_tokens(md_files):
    """Replace '{{Itemizer}}' (allowing optional inner spaces) with '[Itemizer 🛢 helper domain](<../../🛢🤲 Itemizer helper.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Itemizer
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemizer`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Itemizer 🛢 helper domain](<../../🛢🤲 Itemizer helper.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_itemizers_tokens(md_files):
    """Replace '{{Itemizers}}' (allowing optional inner spaces) with '[Itemizer 🛢 helper domains](<../../🛢🤲 Itemizer helper.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Itemizers
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemizers`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Itemizer 🛢 helper domains](<../../🛢🤲 Itemizer helper.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_talker_tokens(md_files):
    """Replace '{{Talker}}' (allowing optional inner spaces) with '[Talker 😃 domain](<😃 Talker role.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Talker
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Talker`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Talker 😃 domain](<😃 Talker role.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_talkers_tokens(md_files):
    """Replace '{{Talkers}}' (allowing optional inner spaces) with '[Talker 😃 domains](<😃 Talker role.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Talkers
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Talkers`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Talker 😃 domains](<😃 Talker role.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_itemized_dataset_tokens(md_files):
    """Replace '{{Itemized dataset}}' (allowing optional inner spaces) with '[Itemized 🪣 dataset](<Itemized 🛢 dataset.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Itemized dataset
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemized dataset`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Itemized 🪣 dataset](<Itemized 🛢 dataset.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_itemized_datasets_tokens(md_files):
    """Replace '{{Itemized datasets}}' (allowing optional inner spaces) with '[Itemized 🪣 datasets](<Itemized 🛢 dataset.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Itemized datasets
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Itemized datasets`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Itemized 🪣 datasets](<Itemized 🛢 dataset.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_notifier_tokens(md_files):
    """Replace '{{Notifier}}' (allowing optional inner spaces) with '[Notifier 📣 domain](<📣👥 Notifier domain.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Notifier
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Notifier`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Notifier 📣 domain](<📣👥 Notifier domain.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_notifiers_tokens(md_files):
    """Replace '{{Notifiers}}' (allowing optional inner spaces) with '[Notifier 📣 domains](<📣👥 Notifier domain.md>)' in all md files."""
    # Allow normal and unicode non-breaking/zero-width spaces around Notifiers
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Notifiers`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Notifier 📣 domains](<📣👥 Notifier domain.md>)"
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = pattern.subn(replacement, content)
        if n > 0:
            try:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                pass
    return total

def replace_prompt_broker_tokens(md_files):
    """Replace '{{Prompt@Broker}}' with '[`Prompt@Broker` 🅰️ method](<relative_path_to_prompt_file>)' in all md files."""
    # Find the target file "🤗🐌🤵 Prompt.md"
    target_file = None
    for path in md_files:
        if os.path.basename(path) == "🤗🐌🤵 Prompt.md":
            target_file = path
            break
    if not target_file:
        return 0  # File not found, no replacements
    
    total = 0
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        if "{{Prompt@Broker}}" in content:
            rel_path = os.path.relpath(target_file, os.path.dirname(md_file))
            replacement = f"[`Prompt@Broker` 🅰️ method](<{rel_path}>)"
            new_content = content.replace("{{Prompt@Broker}}", replacement)
            if new_content != content:
                try:
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    total += 1
                except Exception:
                    pass
    return total

def replace_dynamic_tokens(md_files, file_dict):
    """Replace any remaining {{...}} tokens with links to matching .md files based on normalized names."""
    def replacer(match, file_path):
        token = match.group(1)
        parts = token.split('@', 1)
        if len(parts) == 2:
            # Try after @ first
            file_token = parts[1]
            normalized_token = normalize_string(file_token)
            if normalized_token in file_dict:
                filename, target_path = file_dict[normalized_token]
                rel_path = os.path.relpath(target_path, os.path.dirname(file_path))
                return f"[`{token}`](<{rel_path}>)"
            # If not, try before @
            file_token = parts[0]
            normalized_token = normalize_string(file_token)
            if normalized_token in file_dict:
                filename, target_path = file_dict[normalized_token]
                rel_path = os.path.relpath(target_path, os.path.dirname(file_path))
                return f"[`{token}`](<{rel_path}>)"
        else:
            # No @, use whole token
            file_token = token
            normalized_token = normalize_string(file_token)
            if normalized_token in file_dict:
                filename, target_path = file_dict[normalized_token]
                rel_path = os.path.relpath(target_path, os.path.dirname(file_path))
                return f"[`{token}`](<{rel_path}>)"
        return match.group(0)

    total = 0
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            continue
        new_content, n = re.subn(r'\{\{([^}]+)\}\}', lambda m: replacer(m, file_path), content, flags=re.IGNORECASE)
        if n > 0:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                total += n
            except Exception:
                # Print the exception but continue
                print(f'  Failed to write changes to "file://{file_path.replace(" ", "%20")}"')
                pass

    return total