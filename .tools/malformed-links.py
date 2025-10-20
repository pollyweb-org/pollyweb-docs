# Instructions on how to run this script:
# > python3 -m venv .venv
# > source .venv/bin/activate
# > pip3 install -r requirements.txt
# > cd .tools
# > python3 malformed-links.py

import os
import re
import itertools
from concurrent.futures import ProcessPoolExecutor, as_completed
from collections import OrderedDict

try:
    import emoji as _emoji_mod  # optional dependency
except Exception:
    _emoji_mod = None

all_memory = False

# Globals used by worker processes (initialized via init_worker)
_EXISTING_FILES = None
_PROJECT_DIR = None

# Precompile regex patterns for performance
_LINK_PATTERNS = [
    # match links in the form [text](path.md)
    re.compile(r"\[.*?\]\(([^)]+\.md)\)"),
    # match links in the form [text](<path.md>)
    re.compile(r"\[.*?\]\(<?([^)>]+\.md)>?\)"),
    # images
    re.compile(r"\[.*?\]\(([^)]+\.png)\)"),
    re.compile(r"\[.*?\]\(<?([^)>]+\.png)>?\)"),
    re.compile(r"\[.*?\]\(([^)]+\.jpg)\)"),
    re.compile(r"\[.*?\]\(<?([^)>]+\.jpg)>?\)"),
    re.compile(r"\[.*?\]\(([^)]+\.pdf)\)"),
    re.compile(r"\[.*?\]\(<?([^)>]+\.pdf)>?\)"),
    # match ![](../../../🖼️ images/1.1/ads-market-share.png)
    re.compile(r"!\[\]\(([^)]+?\.(?:png|pdf))\)")
]

_GENERIC_LINK_RE = re.compile(r"(?<!!)\[.*?\]\(<?([^)>#]+)>?\)")
_GENERIC_EXT_RE = re.compile(r"\.(md|png|jpg|pdf)$", re.IGNORECASE)

_MALFORMED_PATTERNS = [
    re.compile(r"\[[^\]]+\]\([^)\n]*\.md(?![^)]*\))"),  # missing closing ')'
    re.compile(r"\[[^\]]+\][^ \[<]+\..+?\)\>?"),       # links not properly closed
    re.compile(r"\[.*?\]\(<?([^)>]+\.md)>(?!\))"),      # not closed
    re.compile(r"\[[^\]]*\.[^\]]*\>\)"),               # missing ']( '
    re.compile(r"!\[.*?\]\([^)\n]+$")                    # image not closed
]

def _init_worker(existing_files, project_dir):
    global _EXISTING_FILES, _PROJECT_DIR
    _EXISTING_FILES = existing_files
    _PROJECT_DIR = project_dir

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
        for pattern in _LINK_PATTERNS:
            links = pattern.findall(line)
            
            for link in links:
                links_with_lines.append((link, i))

                if False and foundTheLine and 'ads-market-share.png' in line:
                   raise ValueError(line)
                   matchedTheLine = True

                if '](.' in line:
                    malformed_links_with_lines.append((line, i))

        # Also capture generic local links without extensions (skip externals/anchors/images)
        generic_links = _GENERIC_LINK_RE.findall(line)
        for link in generic_links:
            # Skip if already a handled extension
            if _GENERIC_EXT_RE.search(link):
                continue
            # Skip external/anchors/mailto
            if link.startswith(('http://', 'https://', 'mailto:', '#')):
                continue
            # Skip pure fragment or empty
            if not link.strip():
                continue
            # Record as a candidate to check existence
            links_with_lines.append((link, i))

        # Find malformed links
        for pattern in _MALFORMED_PATTERNS:
            malformed_links = pattern.findall(line)
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
    ret = ret.replace('$', '')
    ret = ret.replace('✅', '')
    ret = ret.replace('⏳', '')
    ret = ret.replace(' ', '')
    ret = ret.replace('.', '')

    # Also remove TV emojis.
    ret = ret.replace('📺', '')
    ret = ret.replace('🖼️', '')
    ret = ret.replace('🇺🇸', '')
    ret = ret.replace('🇨🇳', '')

    # Optionally remove emojis if 'emoji' module is available
    if _emoji_mod and ('✅' in ret or '⏳' in ret):
        try:
            ret = _emoji_mod.replace_emoji(ret, replace='')
        except Exception:
            pass

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

def _process_single_md_file(md_file):
    """Worker function to process a single Markdown file.

    Returns a tuple: (md_file, broken_list, malformed_list, replacement_hits_list, count)
    """
    import urllib.parse

    broken_list = []
    malformed_list = []
    replacement_hits = []
    count = 0

    # Read file content
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replacement character scans
    if '\ufffd' in content or '�' in content:
        lines = content.splitlines()
        for i, line in enumerate(lines, 1):
            if ('\ufffd' in line) or ('�' in line):
                replacement_hits.append((i, line))

    # Extract links
    links_with_lines, malformed_links_with_lines = extract_links_with_malformed_detection(content)

    # Existing files and project dir from globals
    existing_files = _EXISTING_FILES
    project_directory = _PROJECT_DIR

    # Check links and build suggestions
    for link, line_num in links_with_lines:
        itsTheLine = False
        if '../../../🖼️ images/1.1/ads-market-share.png' in link:
            itsTheLine = True

        full_link = os.path.normpath(os.path.join(os.path.dirname(md_file), link))
        full_link = urllib.parse.unquote(full_link)

        if full_link not in existing_files:
            suggestion = f'!!!'
            tip = None

            if suggestion == '!!!':
                # same-folder heuristic
                x_file_name = os.path.basename(full_link)
                for file in existing_files:
                    if os.path.dirname(full_link) == os.path.dirname(file):
                        y_file_name = os.path.basename(file)
                        if remove_numbers(y_file_name).endswith(remove_numbers(x_file_name)):
                            suggestion = os.path.basename(suggestion)
                            tip = f'File in the same folder?'
                            break

            if suggestion == '!!!':
                # case-insensitive path match
                for file in existing_files:
                    if remove_numbers(full_link).lower() == remove_numbers(file).lower():
                        suggestion = file.replace(project_directory, '')
                        suggestion = os.path.relpath(suggestion, os.path.dirname(md_file))
                        tip = f'Case mismatch?'
                        break

            if suggestion == '!!!':
                # closest match heuristic
                closest_match = max(
                    existing_files,
                    key=lambda x: count_end_match(
                        x.replace(' ','%20'),
                        full_link.replace(' ','%20'))
                )
                x = os.path.normpath(closest_match)
                if remove_numbers(os.path.basename(x)) == remove_numbers(os.path.basename(full_link)) \
                or count_mismatch_chars(os.path.basename(x), os.path.basename(full_link)) <= 1:
                    suggestion = f'{x}'
                    suggestion = os.path.relpath(suggestion, os.path.dirname(md_file))
                    tip = f'Closest match?'

            if suggestion == '!!!':
                # same filename anywhere
                x_file_name = os.path.basename(full_link)
                for file in existing_files:
                    y_file_name = os.path.basename(file)
                    if remove_numbers(y_file_name) == remove_numbers(x_file_name):
                        suggestion = file.replace(project_directory, '')
                        suggestion = os.path.relpath(suggestion, full_link)
                        tip = f'File name match?'
                        break

            if suggestion == '!!!':
                # Try all possible ⏳ emoji insertions into the link path
                emoji_char = '⏳'
                rel_link_path = os.path.relpath(full_link, project_directory)
                for alt_path in possible_emoji_insertions(rel_link_path, emoji=emoji_char):
                    abs_path = os.path.normpath(os.path.join(project_directory, alt_path))
                    if abs_path in existing_files:
                        suggestion = os.path.relpath(abs_path, os.path.dirname(md_file))
                        tip = f"Fix by adding '{emoji_char}' emoji"
                        break

            if link == suggestion:
                suggestion = f'found same'

            if 'https://' in link:
                continue

            tuple_item = (link, full_link, line_num, suggestion, tip)
            if tuple_item not in broken_list:
                broken_list.append(tuple_item)
                count += 1

    # malformed links (per-file)
    if malformed_links_with_lines:
        malformed_list = malformed_links_with_lines

    return (md_file, broken_list, malformed_list, replacement_hits, count)


def check_broken_links(md_files, png_files):
    """Check for broken .md links within the project and malformed links.

    Also scans files for the Unicode replacement character (�, U+FFFD), which
    usually indicates an encoding issue or invalid byte sequence in the file.
    """
    broken_links = OrderedDict()
    malformed_links = OrderedDict()
    replacement_char_hits = OrderedDict()

    existing_files = set(md_files + png_files)

    # Setup multiprocessing pool
    max_workers = os.cpu_count() or 1
    # Initialize workers with shared, read-only data
    with ProcessPoolExecutor(max_workers=max_workers, initializer=_init_worker, initargs=(existing_files, project_directory)) as executor:
        # Use map to preserve order corresponding to md_files
        results_iter = executor.map(_process_single_md_file, md_files)

        total_count = 0
        finished = True
        for md_file, broken_list, malformed_list, replacement_hits, count in results_iter:
            if broken_list:
                broken_links[md_file] = broken_list
                total_count += len(broken_list)
            if malformed_list:
                malformed_links[md_file] = malformed_list
            if replacement_hits:
                replacement_char_hits[md_file] = replacement_hits

            if total_count > 1000 and finished:
                # Emulate original early stop behavior
                print(f"Checking {total_count} times, stopping for performance reasons.")
                finished = False
                break

    return broken_links, malformed_links, replacement_char_hits, finished


def print_results(broken_links, malformed_links, replacement_char_hits):
    """Print the broken and malformed links found in the project and report replacement characters."""

    global all_memory

    if not broken_links and not malformed_links and not replacement_char_hits:
        print("✅✅✅ No issues found! ✅✅✅\n")
    else:
        if broken_links:
            print("## Broken links found in the following files:\n")
            for md_file, links in broken_links.items():
                for link, full_link, line_num, suggestion, tip in links:

                    # Get the relative path of the file, starting from the project directory's parent
                    import os
                    start = os.path.dirname(project_directory + "/../")
                    relative_file = os.path.relpath(md_file, start=os.path.dirname(start))
                    relative_file = f"../{relative_file}"
                    file_name = os.path.basename(md_file)
                    
                    # Create a clickable link with empty [] and <> surrounding the path and line number
                    import urllib.parse
                    import pathlib

                    encoded = urllib.parse.quote(relative_file)
                    file_link = f'[ {file_name} ](<{encoded}#L{line_num}>)'
                    
                    encoded = urllib.parse.quote(file_name)
                    file_name_only= os.path.basename(md_file)
                    encoded = urllib.parse.quote(file_name_only)
                    encoded = urllib.parse.quote(md_file)
                    file_link = f'file://{encoded}, line {line_num}'
                    
                    print(f"\nIn file!: {file_link}")

                    print(f"  - Broken link : <{link}>")
                    print(f"  - Tip         : {tip}")
                    print(f"  - Suggestion  : <{suggestion}>")
                    

                    # Ask the user if they want to fix the link
                    if True and suggestion != '!!!':

                        clean_link = link
                        clean_suggestion = suggestion
                        
                        if '✅ ' in link or '⏳ ' in link:
                            clean_link = remove_numbers(link.replace('<./', '').replace('../', '').replace('./', '').replace('<', '').replace('✅ ', '').replace('⏳ ', '').replace(' ', ''))
                            clean_suggestion = remove_numbers(suggestion.replace('<./', '').replace('../', '').replace('<', '').replace(' ', ''))

                        # Print the cleaned links
                        print('==>' + clean_link)
                        print('==>' + clean_suggestion)
                        
                        fix_link = ''

                        #if '✅ ' in link or '⏳ ' in link:
                        # replace auto-suggested when there's only missing ✅ emojis
                        if clean_suggestion.endswith(clean_link):
                            fix_link = 'y'
                    
                        if fix_link.lower() != 'y':
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
                            elif all_memory:
                                fix_link = 'y'
                            else: 
                                fix_link = input("  - Do you want to fix this link§? (y/n/all): ")
                            
                        if fix_link == "all":
                            all_memory = True
                            fix_link = 'y'

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
                    
                    import urllib.parse
                    import pathlib
                    encoded = urllib.parse.quote(md_file)
                    file_link = f"[ ](<{encoded}#L{line_num}>)"
                    
                    file_link = f"[ ](<{md_file}#L{line_num}>)"

                    import os
                    file_name_only= os.path.basename(md_file)
                    encoded = urllib.parse.quote(file_name_only)
                    encoded = urllib.parse.quote(md_file)
                    file_link = f"file://{encoded}, line {line_num})"

                    print(f"\nIn file±: {file_link}")
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
                            fix_link = input("  - Do you want to fix this link#? (y/n): ")

                        if fix_link.lower() == 'y':
                            # Replace the mal-formatted link with the new link in the file
                            with open(md_file, 'r', encoding='utf-8') as file:
                                content = file.read()
                            new_content = content.replace(malformed_link, suggestion)
                            with open(md_file, 'w', encoding='utf-8') as file:
                                file.write(new_content)
                            print(f"  - Link fixed! ✅")

                            yes_memory.append((malformed_link, suggestion))

        if replacement_char_hits:
            print("\n## Replacement characters (U+FFFD, �) found:")
            for md_file, hits in replacement_char_hits.items():
                for line_num, line_text in hits:
                    import urllib.parse
                    encoded = urllib.parse.quote(md_file)
                    file_link = f"file://{encoded}, line {line_num})"
                    print(f"\nIn file±: {file_link}")
                    print(f"  - Line {line_num}: contains replacement character '�' (U+FFFD)")
                    # Show a trimmed preview to avoid excessive output
                    preview = line_text
                    if len(preview) > 200:
                        preview = preview[:200] + '…'
                    print(f"    Preview: {preview}")


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
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 🏔️ Landscape/2 🧑‍🦰 User Landscape/70. 🔐 Passwordless ID.md",
            "../🖼️ images/PDFs/dkim-rotations.pdf",
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 🏔️ Landscape/🖼️ images/PDFs/dkim-rotations.pdf",
            "<../../🖼️ images/PDFs/dkim-rotations.pdf>",
        ),
        (
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 🏔️ Landscape/2 🧑‍🦰 User Landscape/70. 🔐 Passwordless ID.md",
            "images/some_broken_image.png",
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 🏔️ Landscape/images/some_broken_image.png",
            "<../images/some_broken_image.png>",
        ),
        (
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 🏔️ Landscape/2 🧑‍🦰 User Landscape/70. 🔐 Passwordless ID.md",
            "../../../other_directory/some_file.txt",
            "/Users/jorgemf/AWS/NLWEB/other_directory/some_file.txt",
            "<../../../other_directory/some_file.txt>",
        ),
        (
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 🏔️ Landscape/2 🧑‍🦰 User Landscape/70. 🔐 Passwordless ID.md",
            "71. 🔐 Another ID.md",
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 🏔️ Landscape/2 🧑‍🦰 User Landscape/71. 🔐 Another ID.md",
            "<./71. 🔐 Another ID.md>",
        ),
        (
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 🏔️ Landscape/2 🧑‍🦰 User Landscape/70. 🔐 Passwordless ID.md",
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 🏔️ Landscape/2 🧑‍🦰 User Landscape/71. 🔐 Another ID.md",
            "/Users/jorgemf/AWS/NLWEB/docs/PR-FAQ/1.3 🏔️ Landscape/2 🧑‍🦰 User Landscape/71. 🔐 Another ID.md",
            "<./71. 🔐 Another ID.md>",
        ),
    ]

    for markdown_path, broken_link, correct_full_path, expected_result in test_cases:
        actual_result = fix_markdown_link(markdown_path, broken_link, correct_full_path)
        assert actual_result == expected_result, f"Test failed for: {markdown_path}, {broken_link}, {correct_full_path}. Expected: {expected_result}, Got: {actual_result}"

    print("All tests passed!")


###############################################
# New feature: Convert {{...}} with '@' to markdown links
###############################################

# Capture standard (non-image) markdown links and split text/href
_LINK_WITH_TEXT_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(<?([^)>#]+)>?\)")
_LINK_WITH_TEXT_ANGLE_RE = re.compile(r"(?<!!)\[([^\]]+)\]<([^>#]+)>")
_ANGLE_AUTOLINK_RE = re.compile(r"(?<!!)<?<([^>#]+)>")

# Capture tokens like {{abc@def}} (any text with '@' inside double curly braces)
_CURLY_AT_TOKEN_RE = re.compile(r"\{\{([^{}]*@[^{}]*)\}\}")

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
    """For each md file, replace {{token}} with [`token`](<href>) if a matching link exists.

    Strategy:
    - Prefer links in the same file; if not found, search project-wide index.
    - Keep href as-is but wrap in <...> to be robust with spaces.
    Returns total number of replacements made across the project.
    """
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
            href, base = _pick_matching_link(token, links_here)
            if not href:
                href, base = _pick_matching_link(token, project_index)
            if not href:
                continue

            # If base is not None and not current file, make href relative to current file
            final_href = href
            try:
                if base and base != md_file and not href.startswith(('http://', 'https://', 'mailto:')):
                    # compute absolute path of href based on base file
                    abs_target = os.path.normpath(os.path.join(os.path.dirname(base), href))
                    # convert to path relative to current md_file
                    final_href = os.path.relpath(abs_target, os.path.dirname(md_file))
            except Exception:
                # if anything goes wrong, fallback to original href
                final_href = href

            # Normalize href into (<...>) form
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
                # If writing fails, revert count for this file by recomputing diffs
                pass

    return total_replacements


###############################################
# New feature: Convert {{UPPER}} to markdown links
###############################################

# Match tokens like {{ABC}} where token is uppercase letters/digits/._-
_CURLY_UPPER_TOKEN_RE = re.compile(r"\{\{([A-Z][A-Z0-9._-]*)\}\}")

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


###############################################
# New feature: Prefix table rows with filename emoji
###############################################

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


###############################################
# New feature: Replace {{Placeholder}} with link to $Placeholder 🧠.md
###############################################

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


###############################################
# New feature: Replace {{$.Msg}} with link to $.Msg 📨.md
###############################################

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


###############################################
# New feature: Replace {{Hosts}} with link to Host role.md
###############################################

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


###############################################
# New feature: Replace {{Host}} with link to Host role.md
###############################################

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


###############################################
# New feature: Replace {{Issuer}} with link to Issuer role.md
###############################################

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


###############################################
# New feature: Replace {{Issuers}} with link to Issuer role.md
###############################################

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

    # Re-run until clean or user exits
    while True:
        broken_links, malformed_links, replacement_char_hits, finished = check_broken_links(md_files, png_files)

        # Print the results to "link-issues.md"
        print_results(broken_links, malformed_links, replacement_char_hits)

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



yes_memory = []

if __name__ == "__main__":

    entryPoint = "../../nlweb-docs"
    # Default project directory to PR-FAQ (adjust if necessary)
    project_directory = os.path.abspath(entryPoint)

    # Run the tests
    #test_fix_markdown_link()
    
    runit(project_directory)
