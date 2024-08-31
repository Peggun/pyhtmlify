import argparse
import os
from pathlib import Path
import importlib.util
import sys
from bs4 import BeautifulSoup

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
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
        print(f"Attempting to write HTML content to {output_file}...")

        with output_path.open("w", encoding="utf-8") as file:
            soup = BeautifulSoup(html_content, "html.parser")
            pretty_html = soup.prettify()
            file.write(pretty_html)
            print(f"HTML content successfully written to {output_file}.")
    except Exception as e:
        print(f"Error writing HTML to file {output_file}: {e}")

def generate_html(input_file, output_folder, output_file_name):
    output_folder = Path(output_folder)

    if input_file == "all":
        html_files = list(Path().rglob("html-*.py"))

        if not html_files:
            print("No HTML-related Python files found.")
            return

        for file in html_files:
            html_content = generate_html_from_code(file)

            if html_content:
                file_name = file.with_suffix(".html").name
                write_html_to_file(html_content, output_folder / file_name)
                print(f"HTML file '{file_name}' generated successfully in '{output_folder}'.")
            else:
                print(f"No valid HTML content generated for file {file}.")
    else:
        html_content = generate_html_from_code(input_file)

        if html_content:
            file_name = output_file_name if output_file_name else Path(input_file).with_suffix(".html").name
            write_html_to_file(html_content, output_folder / file_name)
            print(f"HTML file '{file_name}' generated successfully in '{output_folder}'.")
        else:
            print(f"No valid HTML content generated for file {input_file}.")

def find_py_html_files(folder_to_search):
    print("Starting Scan for files to be generated...")

    folder_path = Path(folder_to_search)
    results = []
    for file in folder_path.rglob('html-*.py'):
        results.append({
            'file': file.name,
            'file_path': str(file.resolve())
        })

    num_of_files_found = len(results)
    return results, num_of_files_found

def main():
    parser = argparse.ArgumentParser(
        description="A simple CLI tool for generating HTML using Python."
    )

    parser.add_argument(
        "--version",
        action="version",
        version="pyhtmlify 0.1.8",
        help="Show the version number and exit."
    )

    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")

    generate_parser = subparsers.add_parser(
        "generate",
        help="Generate HTML content from Python files.",
        description="Parses all Python files starting with 'html-' and outputs them into a .html file.",
    )

    generate_parser.add_argument(
        "-f", "--folder", type=str, help="The folder where the output file will be stored.", default="html"
    )

    generate_parser.add_argument(
        "-i", "--input", type=str, help="The single file you would like to generate html with.", default="all"
    )

    generate_parser.add_argument(
        "-n", "--name", type=str, help="The name of the file you would like to generate.", default=""
    )

    find_parser = subparsers.add_parser(
        "find",
        help="Find suitable html-*.py files for conversion along with their respective file paths.",
        description="Find suitable html-*.py files for conversion along with their respective file paths."
    )

    find_parser.add_argument(
        "-f", "--folder", type=str, help="The folder to search for HTML-related Python files.", default=os.getcwd()
    )

    args = parser.parse_args()

    if args.command == "generate":
        generate_html(args.input, args.folder, args.name)
    elif args.command == "find":
        files, num_of_files_found = find_py_html_files(args.folder)
        for file in files:
            print(f"{file['file']} - {file['file_path']}")
        print(f"Found {num_of_files_found} files able to be parsed.")
