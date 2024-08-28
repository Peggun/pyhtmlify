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
        with open(output_file, "w", encoding="utf-8") as file:
            soup = BeautifulSoup(html_content, "html.parser")
            pretty_html = soup.prettify()
            file.write(pretty_html)
    except Exception as e:
        if e is FileNotFoundError:
            raise FileNotFoundError(f"{output_file} wasn't found. Please double check the file path and try again.")

def generate_html(input_file, output_folder, output_file_name):

    if output_file_name:
        if not output_file_name.endswith(".html"):
            output_file_name = output_file_name + ".html"

    print(f"Generating HTML... Outputs will be saved to {output_folder}/{output_file_name}") if output_file_name != "" else output_file_name == None

    os.makedirs(output_folder, exist_ok=True)
    folder = Path(os.getcwd())

    if input_file == "all":

        html_files = [str(file) for file in folder.rglob("html-*.py")]

        if not html_files:
            print("No HTML-related Python files found.")
            return

        for file in html_files:
            html_content = generate_html_from_code(file)
            
            if html_content:
                combined_html = html_content  # Reset for each file

                file_name = file.split("\\")[-1].strip().replace(".py", ".html")

                write_html_to_file(combined_html, os.path.join(output_folder, file_name))
                print(f"HTML file '{file_name}' generated successfully in '{output_folder}'.")

            elif html_content == None:
                raise Exception("No html_content found. Please check if you have forgotten a 'return' statement for your index function")

            else:
                print(f"No valid HTML content generated for file {file}.")

    else:
        html_content = generate_html_from_code(input_file)

        if html_content:
            combined_html = html_content

            if not output_file_name:
                file_name = input_file.split("\\")[-1].strip().replace(".py", ".html")
            else:
                file_name = output_file_name

            write_html_to_file(combined_html, os.path.join(output_folder, file_name))
            print(f"HTML file '{file_name}' generated successfully in '{output_folder}'.")

        elif html_content == None:
            raise Exception("No html_content found. Please check if you have forgotten a 'return' statement for your index function")

        else:
            print(f"No valid HTML content generated for file {file}.")

        
def find_py_html_files(folder_to_search):

    print("Starting Scan for files to be generated...")

    results = []
    num_of_files_found = 0
    for root, dirs, files in os.walk(folder_to_search):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.basename(file_path).startswith('html-') and os.path.basename(file_path).endswith('.py'):
                results.append({
                    'file': file,
                    'file_path': file_path
                })
                num_of_files_found += 1

    return results, num_of_files_found

def main():
    parser = argparse.ArgumentParser(
        description="A simple CLI tool for generating HTML using Python."
    )

    # Add --version option
    parser.add_argument(
        "--version",
        action="version",
        version="pyhtmlify 0.1.7",
        help="Show the version number and exit."
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

    generate_parser.add_argument(
        "-i",
        "--input",
        type=str,
        help="The single file you would like to generate html with.",
        default="all"
    )

    generate_parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="The name of the file you would like to generate.",
        default=""
    )

    find_parser = subparsers.add_parser(
        "find",
        help="Find suitable html-*.py files for conversion along with their respective file paths.",
        description="Find suitable html-*.py files for conversion along with their respective file paths."
    )

    find_parser.add_argument(
        "-f",
        "--folder",
        type=str,
        help="The folder where the output file will be stored.",
        default=os.getcwd(),
    )

    # Parse the arguments
    args = parser.parse_args()

    if args.command == "generate":
        generate_html(args.input, args.folder, args.name)
    if args.command == "find":
        files, num_of_files_found = find_py_html_files(args.folder)
        for file in files:
            print(f"{file['file']} - {file['file_path']}")
        print(f"Found {num_of_files_found} files able to be parsed.")