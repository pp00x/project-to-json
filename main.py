"""This script generates a JSON representation of the project structure in the current directory.

It includes the full content of all files (excluding the script itself).

WARNING: Including the full content of large files can significantly increase the
         size of the output JSON file and may lead to high memory usage.
"""

import os
import json


def generate_project_structure(output_file="project_structure.json"):
    """
    Generates the project structure of the current directory, including the full content
    of all files (excluding the script itself), and saves it as a JSON file.

    Args:
        output_file (str, optional): The name of the JSON file to create.
                                       Defaults to "project_structure.json".
    """

    current_script_path = os.path.abspath(__file__)

    def get_structure(path):
        """
        Recursively explores the directory structure and returns a nested dictionary,
        including file content.
        """
        name = os.path.basename(path)
        if os.path.isfile(path):
            if path == current_script_path:
                return None  # Exclude the script file itself
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except OSError as e:
                content = f"Error reading file: {e}"
            return {"name": name, "type": "file", "content": content}
        elif os.path.isdir(path):
            children = []
            with os.scandir(path) as entries:
                for entry in entries:
                    child_structure = get_structure(entry.path)
                    if child_structure is not None:
                        children.append(child_structure)
            return {"name": name, "type": "directory", "children": children}
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
        f"Project structure with file content (excluding script) "
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
