import os
import urllib.parse

# Hardcoded folder path
FOLDER_PATH = "/Users/jorgemf/Git/NLWeb/docs"
#FOLDER_PATH = "/Users/jorgemf/Git/NLWeb/docs/PR-FAQ"
#FOLDER_PATH = "/Users/jorgemf/Git/NLWeb/docs/PR-FAQ/1.3 ✅ 🏔️ Landscape/2 ✅ 🧑‍🦰 User Landscape/"

def decode_url_encoded_text(text):
    """Decodes any URL-encoded text in the given string."""
    return urllib.parse.unquote(text)

def process_markdown_file(file_path):
    """Reads, decodes, and overwrites a Markdown file with decoded content."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Re-encode to URL format (to simulate what might have been in the original file)
        re_encoded_content = urllib.parse.quote(content)

        decoded_content = decode_url_encoded_text(content)

        if re_encoded_content != content or decoded_content != content:  # Only overwrite if changes are made
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(decoded_content)
            
            #print(f"✔️ Decoded and updated content: {file_path}")
            print("*", end="")

         
        else:
            #print(f"✅ No content changes needed: {file_path}")
            print("-", end="")

            # if 'Delegating.md' in file_path, raise an error
            if 'Delegating.md' in file_path:        

                # if %20 found in content, raise an error
                if "%20" in content:
                    raise ValueError(f"❌ Found URL-encoded text in content: {file_path}")

                #print(content)


    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")

def rename_file_if_needed(file_path):
    """Renames a file if its name contains URL-encoded characters."""
    directory, filename = os.path.split(file_path)
    decoded_filename = decode_url_encoded_text(filename)

    if decoded_filename != filename:
        new_file_path = os.path.join(directory, decoded_filename)
        try:
            os.rename(file_path, new_file_path)
            print(f"🔄 Renamed: {file_path} → {new_file_path}")
            return new_file_path  # Return the new path in case it was renamed
        except Exception as e:
            print(f"❌ Error renaming {file_path}: {e}")
    
    return file_path  # Return original if no rename was done

def process_markdown_files_in_folder(folder_path):
    """Recursively finds and processes all Markdown files in a folder."""
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)

                # Rename the file first (if needed)
                new_file_path = rename_file_if_needed(file_path)

                # Process the content of the renamed or original file
                process_markdown_file(new_file_path)

if __name__ == "__main__":
    if os.path.isdir(FOLDER_PATH):
        print(f"📂 Processing Markdown files in: {FOLDER_PATH}\n")
        process_markdown_files_in_folder(FOLDER_PATH)
        print("\n✅ Processing complete.")
    else:
        print(f"❌ Invalid folder path: {FOLDER_PATH}")
