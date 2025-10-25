"""Output helpers for presenting broken link diagnostics."""

import os
from pathlib import Path
from urllib.parse import quote

from .common import remove_numbers


def print_results(
    broken_links,
    malformed_links,
    replacement_char_hits,
    yes_memory,
    all_memory,
    project_directory,
):
    """Print detected issues and optionally fix links interactively."""
    if not broken_links and not malformed_links and not replacement_char_hits:
        print("✅✅✅ No issues found! ✅✅✅\n")
        return

    if broken_links:
        print("## Broken links found in the following files:\n")
        for md_file, links in broken_links.items():
            for link, full_link, line_num, suggestion, tip in links:
                start = os.path.dirname(project_directory + "/../")
                relative_file = os.path.relpath(md_file, start=os.path.dirname(start))
                relative_file = f"../{relative_file}"
                file_name = os.path.basename(md_file)

                abs_path = Path(md_file).resolve()
                quoted_path = quote(abs_path.as_posix(), safe="/")
                uri = f"vscode://file{quoted_path}:{line_num}"
                display = f"{os.path.relpath(abs_path, project_directory)}:{line_num}"
                file_link = f"\x1b]8;;{uri}\x1b\\{display}\x1b]8;;\x1b\\"

                print(f"\nIn: {file_link}")
                print(f"  - Broken link : <{link}>")
                print(f"  - Tip         : {tip}")
                print(f"  - Suggestion  : <{suggestion}>")

                if suggestion != "!!!":
                    clean_link = link
                    clean_suggestion = suggestion

                    if "✅ " in link or "⏳ " in link:
                        clean_link = remove_numbers(
                            link.replace("<./", "")
                            .replace("../", "")
                            .replace("./", "")
                            .replace("<", "")
                            .replace("✅ ", "")
                            .replace("⏳ ", "")
                            .replace(" ", "")
                        )
                        clean_suggestion = remove_numbers(
                            suggestion.replace("<./", "")
                            .replace("../", "")
                            .replace("<", "")
                            .replace(" ", "")
                        )

                    print("==>" + clean_link)
                    print("==>" + clean_suggestion)

                    fix_link = ""
                    if clean_suggestion.endswith(clean_link):
                        fix_link = "y"

                    if fix_link.lower() != "y":
                        if suggestion == f"../{link}":
                            fix_link = "y"
                        elif link == f"../{suggestion}":
                            fix_link = "y"
                        elif "📺" not in link and suggestion.endswith(link.replace("..", "")):
                            fix_link = "y"
                        elif "📺" not in link and link.endswith(suggestion.replace("..", "")):
                            fix_link = "y"
                        elif "📺" not in link and suggestion.endswith(link.replace("../..", "")):
                            fix_link = "y"
                        elif "📺" not in link and link.endswith(suggestion.replace("../..", "")):
                            fix_link = "y"
                        elif link.lower() == suggestion.lower():
                            fix_link = "y"
                        elif remove_numbers(suggestion) == remove_numbers(link):
                            fix_link = "y"
                        elif yes_memory and (link, suggestion) in yes_memory:
                            fix_link = "y"
                        elif all_memory:
                            fix_link = "y"
                        else:
                            fix_link = input("  - Do you want to fix this link§? (y/n/all): ")

                    if fix_link == "all":
                        all_memory = True
                        fix_link = "y"

                    if fix_link.lower() == "y":
                        with open(md_file, "r", encoding="utf-8") as handle:
                            content = handle.read()
                        new_content = content.replace(f"<{link}>", f"<{suggestion}>")
                        new_content = new_content.replace(f"({link})", f"({suggestion})")
                        with open(md_file, "w", encoding="utf-8") as handle:
                            handle.write(new_content)
                        print("  - Link fixed! ✅")
                        yes_memory.append((link, suggestion))

    if malformed_links:
        print("\n## Malformed links found in the following files:")
        for md_file, links in malformed_links.items():
            for malformed_link, line_num in links:
                abs_path = Path(md_file).resolve()
                quoted_path = quote(abs_path.as_posix(), safe="/")
                uri = f"vscode://file{quoted_path}:{line_num}"
                display = f"{os.path.relpath(abs_path, project_directory)}:{line_num}"
                file_link = f"\x1b]8;;{uri}\x1b\\{display}\x1b]8;;\x1b\\"

                print(f"\nIn: {file_link}")
                print(f"  - Malformed link: {malformed_link}")

                suggestion = None
                fix_link = None

                if (
                    "](" in malformed_link
                    and (
                        ("](../" in malformed_link and ".md)" in malformed_link)
                        or ("](./" in malformed_link and ".md>)" in malformed_link)
                    )
                ):
                    suggestion = (
                        malformed_link.replace("](../", "](<../")
                        .replace("](./", "](<./")
                        .replace(".md)", ".md>)")
                    )
                    print(f"  - Suggestion: {suggestion}")
                    fix_link = "y"
                elif "](../" in malformed_link and ".pdf)" in malformed_link:
                    suggestion = malformed_link.replace("](../", "](<../").replace(".pdf)", ".pdf>)")
                    print(f"  - Suggestion: {suggestion}")
                    fix_link = "y"
                elif "](../" in malformed_link and ".jpg)" in malformed_link:
                    suggestion = malformed_link.replace("](../", "](<../").replace(".jpg)", ".jpg>)")
                    print(f"  - Suggestion: {suggestion}")
                    fix_link = "y"
                elif "](../" in malformed_link and ".png)" in malformed_link:
                    suggestion = malformed_link.replace("](../", "](<../").replace(".png)", ".png>)")
                    print(f"  - Suggestion: {suggestion}")
                    fix_link = "y"

                if suggestion:
                    if fix_link == "y":
                        pass
                    elif yes_memory and (malformed_link, suggestion) in yes_memory:
                        fix_link = "y"
                    elif suggestion == malformed_link.replace("](../", "](<../").replace(".pdf)", ".pdf>)"):
                        fix_link = "y"
                    elif suggestion == malformed_link.replace("](../", "](<../").replace(".jpg)", ".jpg>)"):
                        fix_link = "y"
                    else:
                        fix_link = input("  - Do you want to fix this link#? (y/n): ")

                    if fix_link and fix_link.lower() == "y":
                        with open(md_file, "r", encoding="utf-8") as handle:
                            content = handle.read()
                        new_content = content.replace(malformed_link, suggestion)
                        with open(md_file, "w", encoding="utf-8") as handle:
                            handle.write(new_content)
                        print("  - Link fixed! ✅")
                        yes_memory.append((malformed_link, suggestion))

    if replacement_char_hits:
        print("\n## Replacement characters (U+FFFD, �) found:")
        for md_file, hits in replacement_char_hits.items():
            for line_num, line_text in hits:
                abs_path = Path(md_file).resolve()
                quoted_path = quote(abs_path.as_posix(), safe="/")
                uri = f"vscode://file{quoted_path}:{line_num}"
                display = f"{os.path.relpath(abs_path, project_directory)}:{line_num}"
                file_link = f"\x1b]8;;{uri}\x1b\\{display}\x1b]8;;\x1b\\"
                print(f"\nIn: {file_link}")
                print("  - Contains replacement character '�' (U+FFFD)")
                preview = line_text
                if len(preview) > 200:
                    preview = preview[:200] + "…"
                print(f"    Preview: {preview}")


__all__ = ["print_results"]
