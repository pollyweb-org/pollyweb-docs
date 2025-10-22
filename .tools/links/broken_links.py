import os
import re
import itertools
from concurrent.futures import ProcessPoolExecutor, as_completed
from collections import OrderedDict
import yaml

try:
    import emoji as _emoji_mod  # optional dependency
except Exception:
    _emoji_mod = None

def normalize_string(s):
    # Remove emojis using regex (fallback if emoji library not available)
    s = _GENERAL_EMOJI_RE.sub('', s)
    # Remove spaces and lowercase
    ret = re.sub(r'\s+', '', s).lower()
    ret = ret.replace('$', '')
    return ret

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

_GENERAL_EMOJI_RE = re.compile(
    "[\U0001F1E6-\U0001F1FF\U0001F300-\U0001FAFF\u2190-\u21FF\u2300-\u23FF\u25A0-\u25FF\u2600-\u26FF\u2700-\u27BF\u2B00-\u2BFF]\uFE0F?",
    re.UNICODE,
)

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
    """Recursively find all png/jpg/pdf files in the project directory."""
    png_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".pdf"):
                png_files.append(os.path.join(root, file))
    return png_files

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


def check_broken_links(md_files, png_files, project_directory):
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


def print_results(broken_links, malformed_links, replacement_char_hits, yes_memory, all_memory):
    """Print the broken and malformed links found in the project and report replacement characters."""

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