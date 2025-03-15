"""This script generates a JSON representation of the project structure in the current directory.

It includes the full content of code-related files (excluding the script itself and specified non-code files/folders).

WARNING: Including the full content of large files can significantly increase the
         size of the output JSON file and may lead to high memory usage.
"""

import os
import json

def generate_project_structure(output_file="project_structure.json"):
    """
    Generates the project structure of the current directory, including the full content
    of code-related files (excluding the script itself and specified non-code files/folders),
    and saves it as a JSON file.

    Args:
        output_file (str, optional): The name of the JSON file to create.
                                       Defaults to "project_structure.json".
    """

    current_script_path = os.path.abspath(__file__)
    excluded_folders = [
        "node_modules",
        ".venv",
        ".git",  # Example to exclude .git as well, add more if needed
        "__pycache__", # Example to exclude python cache
    ]
    excluded_files_names = [
        "readme.md",
        "license",
        "LICENSE", # case-insensitive matching is better for file names
        "README.md",
        "README",
        "LICENSE.txt",
    ]
    excluded_extensions = [
        ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".webp", ".bmp",  # Images
        ".mp4", ".mov", ".avi", ".mkv", ".webm",  # Videos
        ".mp3", ".wav", ".ogg", ".flac", ".aac",  # Audio
        ".csv", ".json", ".txt", ".dat", ".sqlite", ".db", ".xml", ".log", ".yaml", ".yml",  # Data/Logs/Configs
        ".zip", ".tar", ".gz", ".rar", ".7z",  # Archives
        ".lock", ".cfg", ".ini", ".toml", ".gitignore", ".DS_Store", ".bak", ".tmp", ".cache", ".DS_Store" # Configs, lock files, temp/system files
    ]
    short_file_size_threshold_kb = 1  # Threshold in KB for considering a file "short"
    short_file_size_threshold_bytes = short_file_size_threshold_kb * 1024


    def get_structure(path):
        """
        Recursively explores the directory structure and returns a nested dictionary,
        including file content for code-related files.
        """
        name = os.path.basename(path).lower() # Lowercase for case-insensitive matching

        if os.path.isdir(path):
            if name in [folder.lower() for folder in excluded_folders]: # Case-insensitive folder exclusion
                return None  # Skip excluded folders
            children = []
            with os.scandir(path) as entries:
                for entry in entries:
                    child_structure = get_structure(entry.path)
                    if child_structure is not None:
                        children.append(child_structure)
            return {"name": name, "type": "directory", "children": children}
        elif os.path.isfile(path):
            if path == current_script_path:
                return None  # Exclude the script file itself

            filename = os.path.basename(path).lower() # Lowercase for case-insensitive matching
            if filename in [f.lower() for f in excluded_files_names]: # Case-insensitive file name exclusion
                return None # Exclude specified file names

            ext = os.path.splitext(path)[1].lower() # Get file extension and lowercase
            if ext in excluded_extensions:
                return None # Exclude files with specified extensions

            if os.path.getsize(path) <= short_file_size_threshold_bytes:
                return None # Exclude short files

            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError as e:
                print(f"Warning: Could not decode file '{path}' as UTF-8. Skipping content.")
                content = None # Or you could set content to a specific string like "<binary content>" or just omit the key.
            except OSError as e:
                content = f"Error reading file: {e}"
            if content is not None:
                return {"name": name, "type": "file", "content": content}
            else:
                 return {"name": name, "type": "file"} # Return file info without content

        else:
            return {"name": name, "type": "unknown"}  # Handle other file system objects

    root_dir = os.getcwd()
    structure = get_structure(root_dir)

    # Ensure the directory exists before writing the file
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(structure, f, indent=4)

    print(
        f"Project structure with code-related file content (excluding script, specified folders/files/extensions, and short files) "
        f"saved to '{output_file}'"
    )
    print(
        "WARNING: Be mindful of the output JSON file size, "
        "especially if your project contains large files."
    )


if __name__ == "__main__":
    output_filename = (
        input(
            "Enter the desired output JSON filename "
            "(default: project_structure.json): "
        )
        or "project_structure.json"
    )
    generate_project_structure(output_filename)