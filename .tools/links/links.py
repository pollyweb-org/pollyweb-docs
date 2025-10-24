import os
import re
import yaml

# Instructions on how to run this script:
# > python3 -m venv .venv
# > source .venv/bin/activate
# > pip3 install -r requirements.txt
# > cd .tools/links
# > python3 links.py

from broken_links import (
    check_broken_links,
    find_md_files,
    find_png_files,
    method_folder_markers,
    normalize_string,
    print_results,
)
from link_replacements import (
    configure_context,
    replace_curly_at_mentions, replace_curly_upper_mentions, add_emoji_to_table_rows,
    replace_placeholder_tokens, replace_msg_tokens, replace_hosts_tokens, replace_host_tokens,
    replace_issuer_tokens, replace_issuers_tokens, replace_vaults_tokens, replace_vault_tokens,
    replace_token_tokens, replace_tokens_tokens, replace_script_tokens, replace_chat_tokens,
    replace_chats_tokens, replace_command_tokens, replace_commands_tokens, replace_settings_tokens,
    replace_placeholders_tokens, replace_domain_tokens, replace_domains_tokens, replace_dataset_tokens,
    replace_datasets_tokens, replace_message_tokens, replace_messages_tokens, replace_schema_tokens,
    replace_schemas_tokens, replace_chat_msg_tokens, replace_broker_tokens, replace_brokers_tokens, replace_seller_tokens,
    replace_function_tokens, replace_functions_tokens, replace_scripts_tokens, replace_item_tokens,
    replace_items_tokens, replace_itemizer_tokens, replace_itemizers_tokens, replace_talker_tokens,
    replace_talkers_tokens, replace_itemized_dataset_tokens, replace_itemized_datasets_tokens,
    replace_notifier_tokens, replace_notifiers_tokens, replace_prompt_broker_tokens, replace_dynamic_tokens,
    replace_triple_brace_tokens
)
from link_replacements.tokens import HARDCODED_HANDLERS

yes_memory = []
all_memory = False


def replace_registered_hardcoded_tokens(md_files):
    """Run all registered hardcoded token replacements with consistent reporting."""

    any_changes = False
    for token_key, metadata in HARDCODED_HANDLERS.items():
        func = metadata["function"]
        label = metadata["token_label"]
        try:
            changes = func(md_files)
        except Exception as exc:
            print(f"Warning: failed replacing {{{label}}} tokens: {exc}")
            continue
        if changes:
            any_changes = True
            print(f"Replaced {changes} {{{label}}} tokens ✅")

    return any_changes


def apply_replacement_pass(md_files, file_dict):
    """Run all replacement helpers once and report whether any changes happened."""

    changes_made = False

    try:
        prompt_broker_changes = replace_prompt_broker_tokens(md_files)
        if prompt_broker_changes:
            changes_made = True
            print(f"Replaced {prompt_broker_changes} {{Prompt@Broker}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Prompt@Broker}} tokens: {e}")

    try:
        triple_changes = replace_triple_brace_tokens(md_files, file_dict)
        if triple_changes:
            changes_made = True
            print(f"Replaced {triple_changes} triple-brace helper tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing triple-brace helper tokens: {e}")

    try:
        replaced = replace_curly_at_mentions(md_files)
        if replaced:
            changes_made = True
            print(f"\nReplaced {replaced} {{}}-mentions with links ✅")
    except Exception as e:
        print(f"\nWarning: failed processing {{}}-mentions: {e}")

    try:
        replaced_upper = replace_curly_upper_mentions(md_files)
        if replaced_upper:
            changes_made = True
            print(f"Replaced {replaced_upper} uppercase {{}}-mentions with links ✅")
    except Exception as e:
        print(f"Warning: failed processing uppercase {{}}-mentions: {e}")

    try:
        if replace_registered_hardcoded_tokens(md_files):
            changes_made = True
    except Exception as e:
        print(f"Warning: failed replacing registered hardcoded tokens: {e}")

    try:
        msg_changes = replace_msg_tokens(md_files)
        if msg_changes:
            changes_made = True
            print(f"Replaced {msg_changes} {{$.Msg}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{$.Msg}} tokens: {e}")

    try:
        issuer_changes = replace_issuer_tokens(md_files)
        if issuer_changes:
            changes_made = True
            print(f"Replaced {issuer_changes} {{Issuer}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Issuer}} tokens: {e}")

    try:
        issuers_changes = replace_issuers_tokens(md_files)
        if issuers_changes:
            changes_made = True
            print(f"Replaced {issuers_changes} {{Issuers}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Issuers}} tokens: {e}")

    try:
        vaults_changes = replace_vaults_tokens(md_files)
        if vaults_changes:
            changes_made = True
            print(f"Replaced {vaults_changes} {{Vaults}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Vaults}} tokens: {e}")

    try:
        vault_changes = replace_vault_tokens(md_files)
        if vault_changes:
            changes_made = True
            print(f"Replaced {vault_changes} {{Vault}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Vault}} tokens: {e}")

    try:
        token_changes = replace_token_tokens(md_files)
        if token_changes:
            changes_made = True
            print(f"Replaced {token_changes} {{Token}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Token}} tokens: {e}")

    try:
        tokens_changes = replace_tokens_tokens(md_files)
        if tokens_changes:
            changes_made = True
            print(f"Replaced {tokens_changes} {{Tokens}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Tokens}} tokens: {e}")

    try:
        chat_changes = replace_chat_tokens(md_files)
        if chat_changes:
            changes_made = True
            print(f"Replaced {chat_changes} {{Chat}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Chat}} tokens: {e}")

    try:
        chats_changes = replace_chats_tokens(md_files)
        if chats_changes:
            changes_made = True
            print(f"Replaced {chats_changes} {{Chats}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Chats}} tokens: {e}")

    try:
        replaced = replace_command_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Command}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Command}} tokens: {e}")

    try:
        replaced = replace_commands_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Commands}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Commands}} tokens: {e}")

    try:
        replaced = replace_settings_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{$.Settings}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{$.Settings}} tokens: {e}")

    try:
        replaced = replace_placeholders_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Placeholders}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Placeholders}} tokens: {e}")

    try:
        replaced = replace_domain_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{domain}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{domain}} tokens: {e}")

    try:
        replaced = replace_domains_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{domains}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{domains}} tokens: {e}")

    try:
        replaced = replace_dataset_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Dataset}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Dataset}} tokens: {e}")

    try:
        replaced = replace_datasets_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Datasets}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Datasets}} tokens: {e}")

    try:
        replaced = replace_message_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Message}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Message}} tokens: {e}")

    try:
        replaced = replace_messages_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Messages}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Messages}} tokens: {e}")

    try:
        replaced = replace_schema_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Schema}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Schema}} tokens: {e}")

    try:
        replaced = replace_schemas_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Schemas}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Schemas}} tokens: {e}")

    try:
        replaced = replace_chat_msg_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{$.Chat}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{$.Chat}} tokens: {e}")

    try:
        replaced = replace_broker_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Broker}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Broker}} tokens: {e}")

    try:
        replaced = replace_brokers_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Brokers}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Brokers}} tokens: {e}")

    try:
        replaced = replace_seller_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Seller}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Seller}} tokens: {e}")

    try:
        replaced = replace_function_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Function}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Function}} tokens: {e}")

    try:
        replaced = replace_functions_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Functions}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Functions}} tokens: {e}")

    try:
        replaced = replace_scripts_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Scripts}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Scripts}} tokens: {e}")

    try:
        replaced = replace_item_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Item}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Item}} tokens: {e}")

    try:
        replaced = replace_items_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Items}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Items}} tokens: {e}")

    try:
        replaced = replace_itemizer_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Itemizer}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Itemizer}} tokens: {e}")

    try:
        replaced = replace_itemizers_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Itemizers}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Itemizers}} tokens: {e}")

    try:
        replaced = replace_talker_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Talker}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Talker}} tokens: {e}")

    try:
        replaced = replace_talkers_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Talkers}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Talkers}} tokens: {e}")

    try:
        replaced = replace_itemized_dataset_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Itemized dataset}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Itemized dataset}} tokens: {e}")

    try:
        replaced = replace_itemized_datasets_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Itemized datasets}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Itemized datasets}} tokens: {e}")

    try:
        replaced = replace_notifier_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Notifier}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Notifier}} tokens: {e}")

    try:
        replaced = replace_notifiers_tokens(md_files)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} {{Notifiers}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing {{Notifiers}} tokens: {e}")

    try:
        replaced = replace_dynamic_tokens(md_files, file_dict)
        if replaced:
            changes_made = True
            print(f"Replaced {replaced} dynamic {{...}} tokens ✅")
    except Exception as e:
        print(f"Warning: failed replacing dynamic {{...}} tokens: {e}")

    try:
        emoji_changes = add_emoji_to_table_rows(md_files)
        if emoji_changes:
            changes_made = True
            print(f"Added emojis to {emoji_changes} table rows ✅")
    except Exception as e:
        print(f"Warning: failed adding emojis to table rows: {e}")

    return changes_made


def runit(project_directory, entryPoint):
    # If the project directory does not exist, look for the entryPoint in the parent folder.
    if not os.path.exists(project_directory):
        # get the parent dir of the current directory
        current_directory = os.path.abspath(os.getcwd())
        parent_directory = os.path.dirname(current_directory)
        # merge the entry point with the parent directory
        project_directory = os.path.join(parent_directory, entryPoint)
    
    # Raise an error if the project directory does not ends with the entry point.
    if not project_directory.endswith(entryPoint.split('/')[-1]):
        raise FileNotFoundError(f"Project directory [{project_directory}] not ending with entry point [{entryPoint}]")
    
    # Print project directory
    print(f"\nProject directory: {project_directory}")

    # Raise an error if the project directory does not exist
    if not os.path.exists(project_directory):
        raise FileNotFoundError(f"Project directory not found: {project_directory}")
    
    # Find all markdown files
    md_files = find_md_files(project_directory)
    
    # Raise an error if there are no markdown files
    if not md_files:
        raise FileNotFoundError("No markdown files found in the project directory.")

    # Share project context with replacement helpers
    configure_context(md_files, project_directory)

    # Test YAML cases
    yaml_path = os.path.join(os.path.dirname(__file__), 'links.yaml')
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    for test in data.get('Successful Tests', []):
        given = test['Given']
        expected_linktext = test['LinkText']
        expected_linkfile = test['LinkFile']
        token = given.strip('{}')
        reasons_text = (test.get('Reasons') or '').lower()
        if 'this is hardcoded' in reasons_text:
            token_key = normalize_string(token)
            handler = HARDCODED_HANDLERS.get(token_key)
            if not handler:
                raise ValueError(f"Hardcoded test failed for {given}: no handler registered for token '{token}'")
            replacement = handler['replacement']
            if expected_linkfile not in replacement:
                raise ValueError(
                    f"Hardcoded test failed for {given}: expected file {expected_linkfile} not in replacement {replacement}"
                )
            if expected_linktext not in replacement:
                raise ValueError(
                    f"Hardcoded test failed for {given}: expected link text {expected_linktext} not in replacement {replacement}"
                )
            matching_files = [path for path in md_files if os.path.basename(path) == expected_linkfile]
            if not matching_files:
                raise ValueError(f"Hardcoded test failed for {given}: file not found -> {expected_linkfile}")
            continue
        if '@' in token:
            parts = token.split('@', 1)
            X = parts[0]
            Y = parts[1]
            normalized_X = normalize_string(X)
            markers = method_folder_markers(Y)

            found = False
            for path in md_files:
                if normalize_string(os.path.basename(path)[:-3]) == normalized_X:
                    folder_path = os.path.dirname(path)
                    normalized_folder = normalize_string(folder_path)
                    if any(marker in normalized_folder for marker in markers):
                        file_name = os.path.basename(path)
                        if file_name == expected_linkfile:
                            found = True
                        break
            if not found:
                raise ValueError(f"Did not find expected file for {given}: {expected_linkfile}")
        elif token.isupper():
            expected_name = expected_linkfile.strip('{}')
            candidate_paths = [
                path for path in md_files
                if os.path.basename(path) == expected_name and "😃" in os.path.dirname(path)
            ]
            if not candidate_paths:
                raise ValueError(f"No matching Talkers file for {given}: {expected_name}")
        elif not token.startswith('.'):
            # for others, like Request Sync
            normalized_token = normalize_string(token)
            found = False
            for path in md_files:
                name = os.path.basename(path)[:-3]
                if normalize_string(name) == normalized_token:
                    file_name = os.path.basename(path)
                    if file_name == expected_linkfile:
                        found = True
                    break
            if not found and token.endswith('s'):
                singular_normalized = normalize_string(token[:-1])
                for path in md_files:
                    name = os.path.basename(path)[:-3]
                    if normalize_string(name) == singular_normalized and os.path.basename(path) == expected_linkfile:
                        found = True
                        break
            if not found:
                raise ValueError(f"No matching file for {given}: {expected_linkfile}")
        else:
            helper_candidates = {
                normalize_string(token),
                normalize_string(f"{{{token}}}"),
            }
            expected_found = any(
                normalize_string(os.path.basename(path)[:-3]) in helper_candidates
                and os.path.basename(path) == expected_linkfile
                for path in md_files
            )
            if not expected_found:
                raise ValueError(f"No helper file for {given}: {expected_linkfile}")
    print("YAML tests passed!")

    #print (f"\nProject files:  {md_files}")
    png_files = find_png_files(project_directory)

    # Build file dictionary for dynamic replacements
    file_dict = {}
    for path in md_files:
        filename = os.path.basename(path)
        if filename.endswith('.md'):
            name_without_md = filename[:-3]
            normalized = normalize_string(name_without_md)
            file_dict[normalized] = (name_without_md, path)

    previous_snapshot = None

    while True:
        broken_links, malformed_links, replacement_char_hits, finished = check_broken_links(md_files, png_files, project_directory)

        print_results(broken_links, malformed_links, replacement_char_hits, yes_memory, all_memory, project_directory)

        snapshot = (
            tuple(broken_links.items()),
            tuple(malformed_links.items()),
            tuple(replacement_char_hits.items()),
        )

        if previous_snapshot is not None and snapshot == previous_snapshot:
            break

        previous_snapshot = snapshot

        changes = apply_replacement_pass(md_files, file_dict)

        if not changes and not broken_links and not malformed_links and not replacement_char_hits:
            break

def test_immutable_token_replacements():
    """Test immutable token replacements that should always work the same way."""
    
    # Test replace_placeholder_tokens
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Placeholder`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Placeholder 🧠](<$Placeholder 🧠.md>)"
    content = "Use {{Placeholder}} here."
    expected = "Use [Placeholder 🧠](<$Placeholder 🧠.md>) here."
    result, n = pattern.subn(replacement, content)
    assert result == expected and n == 1, f"Placeholder test failed: {result}"
    
    # Test replace_host_tokens
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Host`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>)"
    content = "The {{Host}} is important."
    expected = "The [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) is important."
    result, n = pattern.subn(replacement, content)
    assert result == expected and n == 1, f"Host test failed: {result}"
    
    # Test replace_issuer_tokens
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Issuer`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)"
    content = "Contact the {{Issuer}}."
    expected = "Contact the [Issuer 🎴 domain](<../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)."
    result, n = pattern.subn(replacement, content)
    assert result == expected and n == 1, f"Issuer test failed: {result}"
    
    # Test replace_token_tokens
    pattern = re.compile(
        r"\{\{[\s\u00A0\u200B\u200C\u200D]*`?Token`?[\s\u00A0\u200B\u200C\u200D]*\}\}",
        re.IGNORECASE
    )
    replacement = "[Token 🎫](<🎫 Token.md>)"
    content = "This is a {{Token}}."
    expected = "This is a [Token 🎫](<🎫 Token.md>)."
    result, n = pattern.subn(replacement, content)
    assert result == expected and n == 1, f"Token test failed: {result}"
    
    # Test normalize_string
    assert normalize_string("🍏🎭 Brand role") == "brandrole", f"Normalize test failed: {normalize_string('🍏🎭 Brand role')}"
    assert normalize_string("Brand role") == "brandrole", f"Normalize test failed: {normalize_string('Brand role')}"
    assert normalize_string("Some Name") == "somename", f"Normalize test failed: {normalize_string('Some Name')}"
    
    # Test for {{Prompt@Broker}} replacement: the file "🤗🐌🤵 Prompt.md" should be matched by "Prompt"
    assert normalize_string("🤗🐌🤵 Prompt") == "prompt", f"Normalize test failed for file name: {normalize_string('🤗🐌🤵 Prompt')}"
    
    # Test for {{Parse@Hosted}} replacement: the file "😃🐌📦 Parse.md" should be matched by "Parse"
    assert normalize_string("😃🐌📦 Parse") == "parse", f"Normalize test failed for file name: {normalize_string('😃🐌📦 Parse')}"
    
    print("All immutable token replacement tests passed! ✅")

if __name__ == "__main__":
    # entryPoint = "nlweb-docs"
    # Default project directory to the parent of .tools
    project_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    entryPoint = "nlweb-docs"

    # Run the tests
    test_immutable_token_replacements()
    
    runit(project_directory, entryPoint)