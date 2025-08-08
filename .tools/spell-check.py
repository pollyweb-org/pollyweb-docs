import os
import language_tool_python

# Initialize the language tool
tool = language_tool_python.LanguageTool('en-US')

def check_grammar_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        matches = tool.check(content)
        if matches:
            print(f"Grammar issues found in {file_path}:")
            for match in matches:
                print(f"Line {content.count('\\n', 0, match.offset) + 1}: {match.message}")
        else:
            print(f"No grammar issues found in {file_path}.")

def check_grammar_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                check_grammar_in_file(file_path)

# Replace 'your_directory_path' with the path to your project directory
check_grammar_in_directory('.')