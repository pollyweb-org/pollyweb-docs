import os
import re
import itertools

def find_md_files(directory):
    """Recursively find all markdown files in the project directory."""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return md_files

def find_png_files(directory):
    """Recursively find all markdown files in the project directory."""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png") \
            or file.endswith(".jpg") \
            or file.endswith(".pdf") :
                md_files.append(os.path.join(root, file))
    return md_files
    

def extract_links_with_malformed_detection(content):
    """Extract links to .md files and detect malformed ones."""
   
    links_with_lines = []
    malformed_links_with_lines = []
    
    lines = content.splitlines()
    foundTheLine = False
    matchedTheLine = False

    for i, line in enumerate(lines, 1):
        if 'ads-market-share.png' in line:
            foundTheLine = True

        # Find correct links
        for pattern in [
            r'\[.*?\]\(([^)]+\.md)\)', # match links in the form [text](path.md)
            r'\[.*?\]\(<?([^)>]+\.md)>?\)', # match links in the form [text](<path.md>)
            r'\[.*?\]\(([^)]+\.png)\)', # match links in the form [text](path.png)
            r'\[.*?\]\(<?([^)>]+\.png)>?\)', # match links in the form [text](<path.png>)
            r'\[.*?\]\(([^)]+\.jpg)\)', # match links in the form [text](path.png)
            r'\[.*?\]\(<?([^)>]+\.jpg)>?\)', # match links in the form [text](<path.png>)
            r'\[.*?\]\(([^)]+\.pdf)\)', # match links in the form [text](path.png)
            r'\[.*?\]\(<?([^)>]+\.pdf)>?\)', # match links in the form [text](<path.png>)

            # match ![](../../../🖼️ images/1.1/ads-market-share.png)
            r'!\[\]\(([^)]+?\.(?:png|pdf))\)'
        ]:
            links = re.findall(pattern, line)
            
            for link in links:
                links_with_lines.append((link, i))

                if False and foundTheLine and 'ads-market-share.png' in line:
                   raise ValueError(line)
                   matchedTheLine = True

                if '](.' in line:
                    malformed_links_with_lines.append((line, i))

        # Find malformed links
        for patterns in [
            r'\[[^\]]+\][^ \[<]+\..+?\)\>?', # match links that are not closed
            r'\[.*?\]\(<?([^)>]+\.md)>(?!\))', # match links that are not closed
            r'\[[^\]]*\.[^\]]*\>\)' # match links that start with '[' and end with '>)', missing ']('
            
        ]:
            malformed_links = re.findall(patterns, line)
            for malformed_link in malformed_links:

                # Skip links that contain 'http://' or 'https://'
                if 'https://' in malformed_link:
                    links_with_lines.append((malformed_link, i))
                    continue

                # Add the line number to the malformed link
                malformed_links_with_lines.append((malformed_link, i))

    if False and foundTheLine:
        if matchedTheLine:
            raise ValueError(f"MATCHED THE LINE")
        raise ValueError(f"FOUND THE LINE")

    return links_with_lines, malformed_links_with_lines


def count_mismatch_chars(str1, str2):
    # Count the number of mismatched characters between two strings
    # For example ABCD and AB1CD have 1 mismatched character.
    mismatch_count = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            mismatch_count += 1
    return mismatch_count



def count_end_match(str1, str2):
    # Start from the end of both strings and compare characters
    match_length = 0
    min_length = min(len(str1), len(str2))
    
    # Iterate over the characters in reverse order
    for i in range(1, min_length + 1):
        if str1[-i] == str2[-i]:
            match_length += 1
        else:
            break
    
    return match_length


def remove_numbers(string):
    # Remove numbers from the string
    ret = re.sub(r'\d+', '', string)
    ret = ret.replace('✅', '')
    ret = ret.replace('⏳', '')
    ret = ret.replace(' ', '')
    ret = ret.replace('.', '')

    # Also remove TV emojis.
    ret = ret.replace('📺', '')
    ret = ret.replace('🖼️', '')
    ret = ret.replace('🇺🇸', '')
    ret = ret.replace('🇨🇳', '')

    import emoji # type: ignore
    ret = emoji.replace_emoji(ret, replace='')

    return ret

def possible_emoji_insertions(path, emoji='⏳'):
    """
    Yield all possible paths by inserting the emoji '⏳' into file and each folder of a relative path.
    Returns the set of all combinations (including the original).
    """
    path = path.replace('/', os.sep).replace('\\', os.sep)
    path_parts = path.split(os.sep)
    if len(path_parts) == 0:
        return set([path])
    combos = []
    for part in path_parts:
        part = part.strip()
        if emoji in part:
            combos.append([part])
        else:
            # try with and without emoji
            combos.append([part, f"{emoji} {part}"])
    all_combos = set()
    for variant in itertools.product(*combos):
        all_combos.add(os.sep.join(variant))
    return all_combos

def check_broken_links(md_files, png_files):
    """Check for broken .md links within the project and malformed links."""
    broken_links = {}
    malformed_links = {}
    existing_files = set(md_files + png_files)
    
    count = 0
    for md_file in md_files:
        count += 1
        #if count > 10:
        #    # stop
        #    print(f"Checking {count} files, stopping for performance reasons.")
        #    break

        # Read file content
        with open(md_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Extract correct links and malformed links
        links_with_lines, malformed_links_with_lines = extract_links_with_malformed_detection(content)

        # Check if the correct links point to missing files
        for link, line_num in links_with_lines:
            
            itsTheLine = False
            if '../../../🖼️ images/1.1/ads-market-share.png' in link:
                itsTheLine = True
            
            full_link = os.path.normpath(os.path.join(os.path.dirname(md_file), link))
            
            import urllib.parse
            full_link = urllib.parse.unquote(full_link)

            if False and itsTheLine and full_link in existing_files:
                raise ValueError(md_file)

            if full_link not in existing_files:
                
                suggestion = f'!!!'
                tip = None

                if suggestion == '!!!':
                    # Find a file in the same folder that ends with that link name.
                    # Extract the file name from full_link
                    x_file_name = os.path.basename(full_link)
                    # Look for the file name in the existing files
                    for file in existing_files:
                        # Extract the file name from the file path
                        y_file_name = os.path.basename(file)
                        # Check if the file is in the same folder as full_link
                        if os.path.dirname(full_link) == os.path.dirname(file):

                            # Check if the file name matches ends with the file name in full_link
                            if remove_numbers(y_file_name).endswith(remove_numbers(x_file_name)):
                                suggestion = os.path.basename(suggestion)    
                                tip = f'File in the same folder?'
                                break

                if suggestion == '!!!':
                    # Find the same file with different caps (case-insensitive)
                    # Extract the file name from full_link
                    x_file_name = os.path.basename(full_link)
                    # Look for the file name in the existing files
                    for file in existing_files:
                        # Extract the file name from the file path
                        y_file_name = os.path.basename(file)
                        # Check if the file name matches the file name in full_link
                        if remove_numbers(full_link).lower() == remove_numbers(file).lower():
                            # If it matches, then the suggestion is the file path
                            suggestion = file.replace(project_directory, '')
                            suggestion = os.path.relpath(suggestion, os.path.dirname(md_file))
                            tip = f'Case mismatch?'
                            break

                if suggestion == '!!!':
                    # Find the closest match to the broken link.
                    # This is a simple heuristic that can be improved.
                    # The suggestion is the closest file name to the broken link.
                    # The suggestion is case-insensitive.
                    closest_match = max(
                        existing_files, 
                        key=lambda x: count_end_match(
                            x.replace(' ','%20'), 
                            full_link.replace(' ','%20')))
                    x = closest_match.replace(project_directory, '')
                    
                    x = os.path.normpath(closest_match)

                    # if the file name of x contains the same letters as the broken link, then it is a good suggestion
                    if remove_numbers(os.path.basename(x)) == remove_numbers(os.path.basename(full_link)) \
                    or count_mismatch_chars(os.path.basename(x), os.path.basename(full_link)) <= 1:
                        suggestion = f'{x}'
                        suggestion = os.path.relpath(suggestion, os.path.dirname(md_file))
                        tip = f'Closest match?'

                if suggestion == '!!!':
                    # Find the last part of the path in another path prefix.
                    # Extract the file name from full_link
                    x_file_name = os.path.basename(full_link)
                    # Look for the file name in the existing files
                    for file in existing_files:
                        # Extract the file name from the file path
                        y_file_name = os.path.basename(file)
                        # Check if the file name matches the file name in full_link
                        if remove_numbers(y_file_name) == remove_numbers(x_file_name):
                            # If it matches, then the suggestion is the file path
                            suggestion = file.replace(project_directory, '')
                            suggestion = os.path.relpath(suggestion, full_link)
                            tip = f'File name match?'
                            break

                # (NEW) Try all possible ⏳ emoji insertions into the link path
                if suggestion == '!!!':
                    emoji = '⏳'
                    rel_link_path = os.path.relpath(full_link, project_directory)
                    for alt_path in possible_emoji_insertions(rel_link_path, emoji=emoji):
                        # Form the absolute path
                        abs_path = os.path.normpath(os.path.join(project_directory, alt_path))
                        if abs_path in existing_files:
                            suggestion = os.path.relpath(abs_path, os.path.dirname(md_file))
                            tip = f"Fix by adding '{emoji}' emoji"
                            break

                # if link and suggestion are the same, then the suggestion is not found
                if link == suggestion:
                    suggestion = f'found same'

                # Skip links that contain 'http://' or 'https://'
                if 'https://' in link:
                    continue

                # Add the broken link to the dictionary
                if md_file not in broken_links:
                    broken_links[md_file] = []
                    
                tuple = (link, full_link, line_num, suggestion, tip)
                if tuple not in broken_links[md_file]:
                    broken_links[md_file].append(tuple)
        
        # Handle malformed links
        if malformed_links_with_lines:
            malformed_links[md_file] = malformed_links_with_lines
    
    return broken_links, malformed_links


def print_results(broken_links, malformed_links):
    """Print the broken and malformed links found in the project."""
    if not broken_links and not malformed_links:
        print("✅✅✅ No issues found! ✅✅✅\n")
    else:
        if broken_links:
            print("## Broken links found in the following files:\n")
            for md_file, links in broken_links.items():
                for link, full_link, line_num, suggestion, tip in links:

                    # Get the relative path of the file, starting from the project directory's parent
                    start = os.path.dirname(project_directory + "/../")
                    relative_file = os.path.relpath(md_file, start=os.path.dirname(start))
                    relative_file = f"../{relative_file}"
                    file_name = os.path.basename(md_file)
                    
                    # Create a clickable link with empty [] and <> surrounding the path and line number
                    file_link = f'[ {file_name} ](<{relative_file}#L{line_num}>)'
                    print(f"\nIn file: {file_link}")

                    print(f"  - Broken link : <{link}>")
                    print(f"  - Tip         : {tip}")
                    print(f"  - Suggestion  : <{suggestion}>")
                    

                    # Ask the user if they want to fix the link
                    if True and suggestion != '!!!':
                        
                        if suggestion == f'../{link}':
                            fix_link = 'y'
                        elif link == f'../{suggestion}':
                            fix_link = 'y'
                        elif True and '📺' not in link and suggestion.endswith(link.replace('..', '')):
                            fix_link = 'y'
                        elif True and '📺' not in link and link.endswith(suggestion.replace('..', '')):
                            fix_link = 'y'
                        elif True and '📺' not in link and suggestion.endswith(link.replace('../..', '')):
                            fix_link = 'y'
                        elif True and '📺' not in link and link.endswith(suggestion.replace('../..', '')):
                            fix_link = 'y'
                        elif True and link.lower() == suggestion.lower():
                            fix_link = 'y'
                        elif True and remove_numbers(suggestion) == remove_numbers(link):
                            fix_link = 'y'
                        elif yes_memory and (link, suggestion) in yes_memory:
                            fix_link = 'y'
                        else: 
                            fix_link = input("  - Do you want to fix this link? (y/n): ")

                        if fix_link.lower() == 'y':
                            # Replace the broken link with the new link in the file
                            with open(md_file, 'r', encoding='utf-8') as file:
                                content = file.read()
                            new_content = content.replace(f"<{link}>", f"<{suggestion}>")
                            new_content = new_content.replace(f"({link})", f"({suggestion})") # also fix normal links
                            with open(md_file, 'w', encoding='utf-8') as file:
                                file.write(new_content)
                            print(f"  - Link fixed! ✅")

                            yes_memory.append((link, suggestion))
        
        if malformed_links:
            print("\n## Malformed links found in the following files:")
            for md_file, links in malformed_links.items():
                for malformed_link, line_num in links:
                    # Create a clickable link with empty [] and <> surrounding the path and line number
                    file_link = f"[ ](<{md_file}#L{line_num}>)"
                    print(f"\nIn file: {file_link}")
                    print(f"  - Line {line_num}: Malformed link: {malformed_link}")

                    suggestion = None
                    fix_link = None

                    if ('](../' in malformed_link and '.md)' in malformed_link) \
                    or ('](./' in malformed_link and '.md>)' in malformed_link):
                        suggestion = malformed_link
                        suggestion = suggestion.replace('](../', '](<../')
                        suggestion = suggestion.replace('](./', '](<./')
                        suggestion = suggestion.replace('.md)', '.md>)')
                        print(f"  - Suggestion: {suggestion}")
                        fix_link = 'y'

                    elif '](../' in malformed_link and '.pdf)' in malformed_link:
                        suggestion = malformed_link
                        suggestion = suggestion.replace('](../', '](<../')
                        suggestion = suggestion.replace('.pdf)', '.pdf>)')
                        print(f"  - Suggestion: {suggestion}")
                        fix_link = 'y'

                    elif '](../' in malformed_link and '.jpg)' in malformed_link:
                        suggestion = malformed_link
                        suggestion = suggestion.replace('](../', '](<../')
                        suggestion = suggestion.replace('.jpg)', '.jpg>)')
                        print(f"  - Suggestion: {suggestion}")
                        fix_link = 'y'

                    elif '](../' in malformed_link and '.png)' in malformed_link:
                        suggestion = malformed_link
                        suggestion = suggestion.replace('](../', '](<../')
                        suggestion = suggestion.replace('.png)', '.png>)')
                        print(f"  - Suggestion: {suggestion}")
                        fix_link = 'y'

                    if suggestion:

                        if fix_link == 'y':
                            pass
                        elif yes_memory and (malformed_link, suggestion) in yes_memory:
                            fix_link = 'y'
                        elif True and suggestion == malformed_link.replace('](../', '](<../').replace('.pdf)', '.pdf>)'):
                            fix_link = 'y'
                        elif True and suggestion == malformed_link.replace('](../', '](<../').replace('.jpg)', '.jpg>)'):
                            fix_link = 'y'
                        else: 
                            fix_link = input("  - Do you want to fix this link? (y/n): ")

                        if fix_link.lower() == 'y':
                            # Replace the mal-formatted link with the new link in the file
                            with open(md_file, 'r', encoding='utf-8') as file:
                                content = file.read()
                            new_content = content.replace(malformed_link, suggestion)
                            with open(md_file, 'w', encoding='utf-8') as file:
                                file.write(new_content)
                            print(f"  - Link fixed! ✅")

                            yes_memory.append((malformed_link, suggestion))


def fix_markdown_link(markdown_path, broken_link, correct_full_path):
    """
    Fixes a broken relative link in a markdown file.

    Args:
        markdown_path (str): Path to the markdown file.
        broken_link (str): The broken relative link.
        correct_full_path (str): The correct full path to the target.

    Returns:
        str: A new relative link that correctly points to the target.
    """


def fix_markdown_link(markdown_path, broken_link, correct_full_path):
    """
    Fixes a broken relative link in a markdown file.

    Args:
        markdown_path (str): Path to the markdown file.
        broken_link (str): The broken relative link.
        correct_full_path (str): The correct full path to the target.

    Returns:
        str: A new relative link that correctly points to the target.
    """

    markdown_dir = os.path.dirname(markdown_path)
    correct_relative_path = os.path.relpath(correct_full_path, markdown_dir)
    print(f"\n- Markdown Directory: {markdown_dir}")
    print(f"\n- Correct Full Path: {correct_full_path}")
    print(f"\n- Relative Path: {correct_relative_path}")
    return f"<{correct_relative_path}>"


def test_fix_markdown_link():
    """Tests the fix_markdown_link function with various scenarios."""

    test_cases = [
        (
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 ✅ 🏔️ Landscape/2 ✅ 🧑‍🦰 User Landscape/70. ✅ 🔐 Passwordless ID.md",
            "../🖼️ images/PDFs/dkim-rotations.pdf",
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 ✅ 🏔️ Landscape/🖼️ images/PDFs/dkim-rotations.pdf",
            "<../../🖼️ images/PDFs/dkim-rotations.pdf>",
        ),
        (
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 ✅ 🏔️ Landscape/2 ✅ 🧑‍🦰 User Landscape/70. ✅ 🔐 Passwordless ID.md",
            "images/some_broken_image.png",
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 ✅ 🏔️ Landscape/images/some_broken_image.png",
            "<../images/some_broken_image.png>",
        ),
        (
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 ✅ 🏔️ Landscape/2 ✅ 🧑‍🦰 User Landscape/70. ✅ 🔐 Passwordless ID.md",
            "../../../other_directory/some_file.txt",
            "/Users/jorgemf/AWS/NLWEB/other_directory/some_file.txt",
            "<../../../other_directory/some_file.txt>",
        ),
        (
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 ✅ 🏔️ Landscape/2 ✅ 🧑‍🦰 User Landscape/70. ✅ 🔐 Passwordless ID.md",
            "71. ✅ 🔐 Another ID.md",
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 ✅ 🏔️ Landscape/2 ✅ 🧑‍🦰 User Landscape/71. ✅ 🔐 Another ID.md",
            "<./71. ✅ 🔐 Another ID.md>",
        ),
        (
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 ✅ 🏔️ Landscape/2 ✅ 🧑‍🦰 User Landscape/70. ✅ 🔐 Passwordless ID.md",
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 ✅ 🏔️ Landscape/2 ✅ 🧑‍🦰 User Landscape/71. ✅ 🔐 Another ID.md",
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 ✅ 🏔️ Landscape/2 ✅ 🧑‍🦰 User Landscape/71. ✅ 🔐 Another ID.md",
            "<./71. ✅ 🔐 Another ID.md>",
        ),
    ]

    for markdown_path, broken_link, correct_full_path, expected_result in test_cases:
        actual_result = fix_markdown_link(markdown_path, broken_link, correct_full_path)
        assert actual_result == expected_result, f"Test failed for: {markdown_path}, {broken_link}, {correct_full_path}. Expected: {expected_result}, Got: {actual_result}"

    print("All tests passed!")



def runit(project_directory):



    # If the project directory does not it exist, look for the entryPoint in the parent folder.
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

    #print (f"\nProject files:  {md_files}")
    png_files = find_png_files(project_directory)

    # Check for both broken and malformed links
    broken_links, malformed_links = check_broken_links(md_files, png_files)

    # Print the results to "link-issues.md"
    print_results(broken_links, malformed_links)



yes_memory = []

if __name__ == "__main__":

    entryPoint = "../../nlweb-docs"
    # Default project directory to PR-FAQ (adjust if necessary)
    project_directory = os.path.abspath(entryPoint)

    # Run the tests
    #test_fix_markdown_link()
    
    runit(project_directory)
