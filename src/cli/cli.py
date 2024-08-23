import argparse
import os
from pathlib import Path
import importlib.util


def read_python_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""


def execute_python_file(file_path):
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"Error executing file {file_path}: {e}")
        return None


def generate_html_from_code(file_path):
    module = execute_python_file(file_path)
    if module and hasattr(module, "index"):
        try:
            return str(module.index())
        except Exception as e:
            print(f"Error generating HTML from file {file_path}: {e}")
            return ""
    else:
        print(f"No 'index' function found in the provided file {file_path}.")
        return ""


def write_html_to_file(html_content, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(html_content)
    except Exception as e:
        print(f"Error writing to file {output_file}: {e}")


def generate_html(output_folder):
    print(f"Generating HTML... Outputs will be saved to {output_folder}/")

    os.makedirs(output_folder, exist_ok=True)

    # Find all Python files starting with 'html-' in the current directory and subdirectories
    folder = Path(os.getcwd())
    html_files = [str(file) for file in folder.rglob("html-*.py")]

    if not html_files:
        print("No HTML-related Python files found.")
        return

    # Combine HTML contents from all files
    combined_html = ""
    for file in html_files:

        combined_html = ""

        html_content = generate_html_from_code(file)
        if html_content:
            combined_html += html_content + "\n"

        file_name = file.split("\\")[-1].strip().replace(".py", ".html")

        print(os.path.join(output_folder, file_name))

        if combined_html:
            # Write the combined HTML to the output file
            write_html_to_file(combined_html, os.path.join(output_folder, file_name))
            print(
                f"HTML file '{file_name}' generated successfully in '{output_folder}'."
            )
        else:
            print("No valid HTML content generated.")


def main():
    parser = argparse.ArgumentParser(
        description="A simple CLI tool for generating HTML using Python."
    )

    # Define subcommands
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")

    # Add 'generate' subcommand with a description
    generate_parser = subparsers.add_parser(
        "generate",
        help="Generate HTML content from Python files.",
        description="Parses all Python files starting with 'html-' and outputs them into a .html file.",
    )

    generate_parser.add_argument(
        "-f",
        "--folder",
        type=str,
        help="The folder where the output file will be stored.",
        default="html",
    )
    # Parse the arguments
    args = parser.parse_args()

    if args.command == "generate":
        generate_html(args.folder)
