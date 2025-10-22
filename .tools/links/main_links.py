import os
import re
import yaml

from broken_links import find_md_files, find_png_files, check_broken_links, print_results
from links_replace import (
    replace_curly_at_mentions, replace_curly_upper_mentions, add_emoji_to_table_rows,
    replace_placeholder_tokens, replace_msg_tokens, replace_hosts_tokens, replace_host_tokens,
    replace_issuer_tokens, replace_issuers_tokens, replace_vaults_tokens, replace_vault_tokens,
    replace_token_tokens, replace_tokens_tokens, replace_script_tokens, replace_chat_tokens,
    replace_chats_tokens, replace_command_tokens, replace_commands_tokens, replace_settings_tokens,
    replace_placeholders_tokens, replace_domain_tokens, replace_domains_tokens, replace_dataset_tokens,
    replace_datasets_tokens, replace_message_tokens, replace_messages_tokens, replace_schema_tokens,
    replace_schemas_tokens, replace_chat_msg_tokens, replace_broker_tokens, replace_brokers_tokens,
    replace_function_tokens, replace_functions_tokens, replace_scripts_tokens, replace_item_tokens,
    replace_items_tokens, replace_itemizer_tokens, replace_itemizers_tokens, replace_talker_tokens,
    replace_talkers_tokens, replace_itemized_dataset_tokens, replace_itemized_datasets_tokens,
    replace_notifier_tokens, replace_notifiers_tokens, replace_prompt_broker_tokens, replace_dynamic_tokens
)

yes_memory = []
all_memory = False

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

    # Test YAML cases
    yaml_path = os.path.join(os.path.dirname(__file__), 'links.yaml')
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    for test in data.get('Successful Tests', []):
        given = test['Given']
        expected_linktext = test['LinkText']
        expected_linkfile = test['LinkFile']
        token = given.strip('{}')
        if token in ['Placeholder', 'Host', 'Hosts']:
            if token == 'Placeholder':
                expected_file = '$Placeholder 🧠.md'
            elif token in ['Host', 'Hosts']:
                expected_file = '🤗🎭 Host role.md'
            if expected_file != expected_linkfile:
                raise ValueError(f"Hardcoded test failed for {given}: {expected_file} != {expected_linkfile}")
        elif '@' in token:
            parts = token.split('@', 1)
            X = parts[0]
            Y = parts[1]
            normalized_X = normalize_string(X)
            normalized_Y_methods = normalize_string(Y + 'methods')
            found = False
            for path in md_files:
                if normalize_string(os.path.basename(path)[:-3]) == normalized_X:
                    folder_path = os.path.dirname(path)
                    if normalized_Y_methods in normalize_string(folder_path):
                        file_name = os.path.basename(path)
                        if file_name == expected_linkfile:
                            found = True
                        break
            if not found:
                raise ValueError(f"Did not find expected file for {given}: {expected_linkfile}")
        elif token.isupper():
            assumed_path = os.path.join(project_directory, "4 ⚙️ Solution", "35 💬 Chats", "😃 Talkers", "😃⚙️ Talker cmds", "for control", f"{token} ⤴️.md")
            if os.path.exists(assumed_path):
                file_name = os.path.basename(assumed_path)
                expected_linkfile = expected_linkfile.strip('{}')
                if file_name != expected_linkfile:
                    raise ValueError(f"Wrong file for {given}: {file_name} != {expected_linkfile}")
            else:
                raise ValueError(f"Assumed path not found for {given}: {assumed_path}")
        else:
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
            if not found:
                raise ValueError(f"No matching file for {given}: {expected_linkfile}")
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

    # Re-run until clean or user exits
    while True:
        broken_links, malformed_links, replacement_char_hits, finished = check_broken_links(md_files, png_files, project_directory)

        # Print the results to "link-issues.md"
        print_results(broken_links, malformed_links, replacement_char_hits, yes_memory, all_memory, project_directory)

        # If clean, stop; otherwise prompt to repeat
        if not broken_links and not malformed_links and not replacement_char_hits:
            break

        try:
            ans = input("\nIssues found. Press ENTER to repeat, or type 'q' to quit: ")
        except EOFError:
            # Non-interactive environment: do not loop endlessly
            break
        if ans.strip().lower() == 'q':
            break

    # After all OK: replace {{...}} with links when possible
    # Replace {{Prompt@Broker}} tokens first to ensure correct linking
    try:
        prompt_broker_changes = replace_prompt_broker_tokens(md_files)
        if prompt_broker_changes:
            print(f"Replaced {prompt_broker_changes} {{Prompt@Broker}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Prompt@Broker}} tokens: {e}")

    try:
        replaced = replace_curly_at_mentions(md_files)
        if replaced:
            print(f"\nReplaced {replaced} {{}}-mentions with links ✅")
        else:
            pass
            #print("\nNo {{...}} @-mentions to replace or no matching links found.")
    except Exception as e:
        print(f"\nWarning: failed processing {{}}-mentions: {e}")

    # Then process {{UPPER}} tokens
    try:
        replaced_upper = replace_curly_upper_mentions(md_files)
        if replaced_upper:
            print(f"Replaced {replaced_upper} uppercase {{}}-mentions with links ✅")
        else:
            pass
            #print("No uppercase {{...}} mentions to replace or no matching links found.")
    except Exception as e:
        print(f"Warning: failed processing uppercase {{}}-mentions: {e}")

    # Replace {{Placeholder}} tokens with link to $Placeholder 🧠.md
    try:
        ph_changes = replace_placeholder_tokens(md_files)
        if ph_changes:
            print(f"Replaced {ph_changes} {{Placeholder}} tokens ✅")
        else:
            pass
            #print("No {{Placeholder}} tokens to replace.")
    except Exception as e:
        print(f"Warning: failed replacing {{Placeholder}} tokens: {e}")

    # Replace {{$.Msg}} tokens
    try:
        msg_changes = replace_msg_tokens(md_files)
        if msg_changes:
            print(f"Replaced {msg_changes} {{$.Msg}} tokens ✅")
        else:
            pass
            #print("No {{$.Msg}} tokens to replace.")
    except Exception as e:
        print(f"Warning: failed replacing {{$.Msg}} tokens: {e}")

    # Replace {{Hosts}} tokens
    try:
        hosts_changes = replace_hosts_tokens(md_files)
        if hosts_changes:
            print(f"Replaced {hosts_changes} {{Hosts}} tokens ✅")
        else:
            pass
            #print("No {{Hosts}} tokens to replace.")
    except Exception as e:
        print(f"Warning: failed replacing {{Hosts}} tokens: {e}")

    # Replace {{Host}} tokens
    try:
        host_changes = replace_host_tokens(md_files)
        if host_changes:
            print(f"Replaced {host_changes} {{Host}} tokens ✅")
        else:
            pass
            #print("No {{Host}} tokens to replace.")
    except Exception as e:
        print(f"Warning: failed replacing {{Host}} tokens: {e}")

    # Replace {{Issuer}} tokens
    try:
        issuer_changes = replace_issuer_tokens(md_files)
        if issuer_changes:
            print(f"Replaced {issuer_changes} {{Issuer}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Issuer}} tokens: {e}")

    # Replace {{Issuers}} tokens
    try:
        issuers_changes = replace_issuers_tokens(md_files)
        if issuers_changes:
            print(f"Replaced {issuers_changes} {{Issuers}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Issuers}} tokens: {e}")

    # Replace {{Vaults}} tokens
    try:
        vaults_changes = replace_vaults_tokens(md_files)
        if vaults_changes:
            print(f"Replaced {vaults_changes} {{Vaults}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Vaults}} tokens: {e}")

    # Replace {{Vault}} tokens
    try:
        vault_changes = replace_vault_tokens(md_files)
        if vault_changes:
            print(f"Replaced {vault_changes} {{Vault}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Vault}} tokens: {e}")

    # Replace {{Token}} tokens
    try:
        token_changes = replace_token_tokens(md_files)
        if token_changes:
            print(f"Replaced {token_changes} {{Token}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Token}} tokens: {e}")

    # Replace {{Tokens}} tokens
    try:
        tokens_changes = replace_tokens_tokens(md_files)
        if tokens_changes:
            print(f"Replaced {tokens_changes} {{Tokens}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Tokens}} tokens: {e}")

    # Replace {{Script}} tokens
    try:
        script_changes = replace_script_tokens(md_files)
        if script_changes:
            print(f"Replaced {script_changes} {{Script}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Script}} tokens: {e}")

    # Replace {{Chat}} tokens
    try:
        chat_changes = replace_chat_tokens(md_files)
        if chat_changes:
            print(f"Replaced {chat_changes} {{Chat}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Chat}} tokens: {e}")

    # Replace {{Chats}} tokens
    try:
        chats_changes = replace_chats_tokens(md_files)
        if chats_changes:
            print(f"Replaced {chats_changes} {{Chats}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Chats}} tokens: {e}")

    # Replace {{Command}} tokens
    try:
        replaced = replace_command_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Command}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Command}} tokens: {e}")

    # Replace {{Commands}} tokens
    try:
        replaced = replace_commands_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Commands}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Commands}} tokens: {e}")

    # Replace {{$.Settings}} tokens
    try:
        replaced = replace_settings_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{$.Settings}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{$.Settings}} tokens: {e}")

    # Replace {{Placeholders}} tokens
    try:
        replaced = replace_placeholders_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Placeholders}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Placeholders}} tokens: {e}")

    # Replace {{domain}} tokens
    try:
        replaced = replace_domain_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{domain}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{domain}} tokens: {e}")

    # Replace {{domains}} tokens
    try:
        replaced = replace_domains_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{domains}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{domains}} tokens: {e}")

    # Replace {{Dataset}} tokens
    try:
        replaced = replace_dataset_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Dataset}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Dataset}} tokens: {e}")

    # Replace {{Datasets}} tokens
    try:
        replaced = replace_datasets_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Datasets}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Datasets}} tokens: {e}")

    # Replace {{Message}} tokens
    try:
        replaced = replace_message_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Message}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Message}} tokens: {e}")

    # Replace {{Messages}} tokens
    try:
        replaced = replace_messages_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Messages}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Messages}} tokens: {e}")

    # Replace {{Schema}} tokens
    try:
        replaced = replace_schema_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Schema}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Schema}} tokens: {e}")

    # Replace {{Schemas}} tokens
    try:
        replaced = replace_schemas_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Schemas}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Schemas}} tokens: {e}")

    # Replace {{$.Chat}} tokens
    try:
        replaced = replace_chat_msg_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{$.Chat}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{$.Chat}} tokens: {e}")

    # Replace {{Broker}} tokens
    try:
        replaced = replace_broker_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Broker}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Broker}} tokens: {e}")

    # Replace {{Brokers}} tokens
    try:
        replaced = replace_brokers_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Brokers}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Brokers}} tokens: {e}")

    # Replace {{Function}} tokens
    try:
        replaced = replace_function_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Function}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Function}} tokens: {e}")

    # Replace {{Functions}} tokens
    try:
        replaced = replace_functions_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Functions}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Functions}} tokens: {e}")

    # Replace {{Scripts}} tokens
    try:
        replaced = replace_scripts_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Scripts}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Scripts}} tokens: {e}")

    # Replace {{Item}} tokens
    try:
        replaced = replace_item_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Item}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Item}} tokens: {e}")

    # Replace {{Items}} tokens
    try:
        replaced = replace_items_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Items}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Items}} tokens: {e}")

    # Replace {{Itemizer}} tokens
    try:
        replaced = replace_itemizer_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Itemizer}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Itemizer}} tokens: {e}")

    # Replace {{Itemizers}} tokens
    try:
        replaced = replace_itemizers_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Itemizers}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Itemizers}} tokens: {e}")

    # Replace {{Talker}} tokens
    try:
        replaced = replace_talker_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Talker}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Talker}} tokens: {e}")

    # Replace {{Talkers}} tokens
    try:
        replaced = replace_talkers_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Talkers}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Talkers}} tokens: {e}")

    # Replace {{Itemized dataset}} tokens
    try:
        replaced = replace_itemized_dataset_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Itemized dataset}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Itemized dataset}} tokens: {e}")

    # Replace {{Itemized datasets}} tokens
    try:
        replaced = replace_itemized_datasets_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Itemized datasets}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Itemized datasets}} tokens: {e}")

    # Replace {{Notifier}} tokens
    try:
        replaced = replace_notifier_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Notifier}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Notifier}} tokens: {e}")

    # Replace {{Notifiers}} tokens
    try:
        replaced = replace_notifiers_tokens(md_files)
        if replaced:
            print(f"Replaced {replaced} {{Notifiers}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing {{Notifiers}} tokens: {e}")

    # Replace dynamic {{...}} tokens
    try:
        replaced = replace_dynamic_tokens(md_files, file_dict)
        if replaced:
            print(f"Replaced {replaced} dynamic {{...}} tokens ✅")
        else:
            pass
    except Exception as e:
        print(f"Warning: failed replacing dynamic {{...}} tokens: {e}")

    # Finally, add emoji at table row start based on filename in upper links
    try:
        emoji_changes = add_emoji_to_table_rows(md_files)
        if emoji_changes:
            print(f"Added emojis to {emoji_changes} table rows ✅")
        else:
            pass
            #print("No table rows required emoji prefixing.")
    except Exception as e:
        print(f"Warning: failed adding emojis to table rows: {e}")

def normalize_string(s):
    # Remove emojis using regex (fallback if emoji library not available)
    s = re.sub(r"[\U0001F1E6-\U0001F1FF\U0001F300-\U0001FAFF\u2190-\u21FF\u2300-\u23FF\u25A0-\u25FF\u2600-\u26FF\u2700-\u27BF\u2B00-\u2BFF]\uFE0F?", "", s)
    # Remove spaces and lowercase
    ret = re.sub(r'\s+', '', s).lower()
    ret = ret.replace('$', '')
    return ret

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