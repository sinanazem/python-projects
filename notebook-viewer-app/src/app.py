import streamlit as st
import os
from pathlib import Path



def list_subdirectories(root_dir):
    """List subdirectories in the given root directory."""
    return [name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name))]

def list_html_files(directory):
    """List all HTML files in the given directory."""
    return [name for name in os.listdir(directory) if name.endswith('.html')]

def load_html_content(file_path):
    """Load HTML content from the specified file path."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    st.title("Jupyter Notebooks Viewer")

    # Root directory containing all the folders and subfolders of HTML files
    ROOT_DIR = Path(".").resolve() / 'HTML_Lectures'

    # List all subdirectories in the root directory
    subdirectories = list_subdirectories(ROOT_DIR)

    # Allow users to select a subdirectory
    selected_directory = st.sidebar.selectbox("Select a folder:", subdirectories)

    if selected_directory:
        # Path to the selected directory
        selected_dir_path = os.path.join(ROOT_DIR, selected_directory)

        # List all HTML files in the selected directory
        html_files = list_html_files(selected_dir_path)

        # Allow user to select an HTML file
        selected_html_file = st.sidebar.selectbox("Select a notebook:", html_files)

        if selected_html_file:
            # Full path to the selected HTML file
            html_file_path = os.path.join(selected_dir_path, selected_html_file)

            # Load and display the HTML content
            html_content = load_html_content(html_file_path)
            st.components.v1.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()

