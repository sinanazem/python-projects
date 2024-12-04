import os
import shutil
from nbconvert import HTMLExporter
import nbformat
from pathlib import Path

def convert_notebook_to_html(notebook_path, output_path):
    """Convert a single Jupyter Notebook to HTML."""
    with open(notebook_path, 'r', encoding='utf-8') as nb_file:
        notebook_content = nbformat.read(nb_file, as_version=4)

    html_exporter = HTMLExporter()
    # Optionally remove code inputs
    # html_exporter.exclude_input = True

    (body, resources) = html_exporter.from_notebook_node(notebook_content)

    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(body)

def ensure_directory_exists(file_path):
    """Ensure the directory for a file path exists."""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def convert_all_notebooks(src_root, dst_root):
    """Recursively convert all .ipynb files in src_root to HTML files in dst_root."""
    for dirpath, _, filenames in os.walk(src_root):
        for filename in filenames:
            if filename.endswith('.ipynb'):
                src_notebook_path = os.path.join(dirpath, filename)
                
                # Determine the relative path and equivalent HTML output path
                relative_path = os.path.relpath(dirpath, src_root)
                dst_dir = os.path.join(dst_root, relative_path)
                html_filename = os.path.splitext(filename)[0] + '.html'
                dst_html_path = os.path.join(dst_dir, html_filename)

                # Ensure the equivalent HTML directory exists
                ensure_directory_exists(dst_html_path)

                # Convert the notebook and save it
                convert_notebook_to_html(src_notebook_path, dst_html_path)
                print(f"Converted: {src_notebook_path} to {dst_html_path}")

if __name__ == "__main__":
           
    src_directory = Path(".").resolve() / "Lectures"
    dst_directory = Path(".").resolve() / "HTML_Lectures"    

    # Perform conversion
    convert_all_notebooks(src_directory, dst_directory)