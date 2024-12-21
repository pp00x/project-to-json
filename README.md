# Project Structure to JSON

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.7+-brightgreen.svg)](https://www.python.org/downloads/)

**Effortlessly capture the blueprint of your project's organization with a single command.**

This Python script provides a convenient way to generate a JSON representation of your project's directory structure. It delves into each directory, listing files and subdirectories, offering a comprehensive snapshot of your project's architecture. Furthermore, it includes the complete content of each file directly within the JSON output, making it a powerful tool for certain documentation or analysis tasks.

**Key Features:**

*   **Detailed Structure:**  Generates a hierarchical JSON representation mirroring your project's file system.
*   **File Content Inclusion:**  Embeds the full content of each file (excluding the script itself) within the JSON output. This is particularly useful for analyzing small to medium-sized projects or specific configurations.
*   **User-Friendly Output:**  Produces a well-formatted JSON file with indentation for easy readability.
*   **Customizable Output Filename:**  Allows you to specify the name of the output JSON file when running the script.
*   **Error Handling:** Gracefully handles potential errors during file reading, such as permission issues, by including an error message in the JSON output.

**Usage:**

1. **Save the script:** Save the provided Python code to a file named, for instance, `generate_structure.py`, within the root directory of the project you want to analyze.

2. **Navigate to your project:** Open your terminal or command prompt and navigate to the root directory of your project.

3. **Run the script:** Execute the script using Python:

    ```bash
    python generate_structure.py
    ```

4. **Specify output filename (optional):** The script will prompt you to enter the desired output JSON filename. If you press Enter without typing a name, it will default to `project_structure.json`.

    ```
    Enter the desired output JSON filename (default: project_structure.json): my_project_layout.json
    ```

5. **Output generated:** The script will create a JSON file (e.g., `my_project_layout.json`) in the same directory, containing the structure and file contents.

**Example Output:**

```json
{
    "name": "my_project",
    "type": "directory",
    "children": [
        {
            "name": ".gitignore",
            "type": "file",
            "content": "# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n\n# C extensions on Windows...\n"
        },
        {
            "name": "src",
            "type": "directory",
            "children": [
                {
                    "name": "main.py",
                    "type": "file",
                    "content": "def hello_world():\n    print(\"Hello, world!\")\n\nif __name__ == \"__main__\":\n    hello_world()\n"
                },
                {
                    "name": "utils.py",
                    "type": "file",
                    "content": "def add(a, b):\n    return a + b\n"
                }
            ]
        },
        {
            "name": "README.md",
            "type": "file",
            "content": "# My Project\n\nA simple example project.\n"
        }
    ]
}

```
**Important Considerations:**

*   **File Size and Memory Usage:** As highlighted in the initial warning, including the full content of all files can lead to significantly large JSON files, especially for projects with large assets (e.g., images, videos, large data files). This can consume a considerable amount of memory during script execution. Exercise caution when running this script on projects with substantial file sizes.
*   **Excluding Specific Files/Directories:** The current script includes all files and directories except for the script itself. For more complex scenarios, you might need to modify the script to exclude specific file types or directories based on your needs.
*   **Security:** Be mindful of the sensitive information that might be included in your files. Ensure that the generated JSON file is handled securely, especially if it contains API keys, passwords, or other confidential data.

**Potential Use Cases:**

*   **Documentation:** Quickly generate a snapshot of your project structure for documentation purposes.
*   **Analysis:** Analyze the organization and content of a project programmatically.
*   **Configuration Backup:** Create a JSON backup of your project's configuration files (with the caveat of potential size).
*   **Educational Tool:** Visualize and understand the structure of different projects.

**Contributing:**

Contributions to enhance this script are welcome! Feel free to submit pull requests for improvements, bug fixes, or new features.

**License:**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Author:**

[Prashant Patil/pp00x]