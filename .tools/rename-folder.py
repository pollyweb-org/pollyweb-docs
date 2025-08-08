import os
import sys

def rename_subfolder_and_update_references(project_folder, current_name, new_name):
    # Define the full paths for the current and new subfolder
    current_folder_path = os.path.join(project_folder, current_name)
    new_folder_path = os.path.join(project_folder, new_name)

    # Check if the current folder exists
    if not os.path.isdir(current_folder_path):
        print(f"Error: The folder '{current_name}' does not exist in '{project_folder}'.")
        return

    # Step 1: Update all references to the files inside the current subfolder in all *.md files
    for root, _, files in os.walk(project_folder):
        for file in files:
            # Look for markdown files only
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace all references to the current folder
                updated_content = content.replace(f'/{current_name}/', f'/{new_name}/')
                
                # Only write if there are changes
                if updated_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"Updated references in {file_path}")

    # Step 2: Rename the subfolder
    os.rename(current_folder_path, new_folder_path)
    print(f"Renamed folder '{current_name}' to '{new_name}'")

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python rename_subfolder.py <project_folder> <current_name> <new_name>")
    else:
        project_folder = sys.argv[1]
        current_name = sys.argv[2]
        new_name = sys.argv[3]
        rename_subfolder_and_update_references(project_folder, current_name, new_name)
