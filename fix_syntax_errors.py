import os
import ast

def remove_syntax_errors_from_file(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
        # Try parsing file
        ast.parse(''.join(lines))
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        # Remove the problematic line
        lineno = e.lineno
        if lineno is not None and 0 < lineno <= len(lines):
            del lines[lineno - 1]
            print(f"Removed line {lineno} from {filepath}")
            with open(filepath, 'w') as file:
                file.writelines(lines)
    except Exception as e:
        print(f"Unhandled error in {filepath}: {e}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                remove_syntax_errors_from_file(filepath)

if __name__ == "__main__":
    process_directory(".")
