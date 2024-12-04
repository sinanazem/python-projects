# Jupyter Notebook HTML Converter and Viewer
<img src="https://www.adobe.com/uk/acrobat/resources/document-files/text-files/media_171e0b0e52c88c407fa45279fe385fd1b88dd4412.png?width=750&format=png&optimize=medium">
This project provides a simple solution for converting Jupyter Notebooks (`.ipynb`) to HTML format and viewing them through a Streamlit application. It automates the conversion of notebooks located in a specified folder into HTML files, maintaining the original folder structure, and offers a Streamlit-based user interface to view them.

## Prerequisites

- Python 3.x
- Jupyter (for `nbconvert`)
- Streamlit

## Installation

1. Clone this repository and navigate into it:

    ```bash
    git clone https://github.com/sinanazem/notebook-viewr-app.git
    cd yourrepository
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

   Ensure your `requirements.txt` includes at least:
   ```
   nbformat
   nbconvert
   streamlit
   ```

## Usage

### Step 1: Convert Notebooks to HTML

1. Place all your Jupyter Notebooks inside the `Lectures` folder. The structure can include multiple subfolders.

2. Run the conversion script to convert all notebooks to HTML while preserving the folder structure:

    ```bash
    python convert_to_html.py.py
    ```

   After this step, you'll have a new `html` directory mirroring the `Lectures` directory structure with HTML files.

### Step 2: View HTML in Streamlit

1. Run the Streamlit application to view the converted HTML files:

    ```bash
    streamlit run app.py
    ```

2. Open a web browser and go to the URL provided by Streamlit, typically `http://localhost:8501`.

3. Use the sidebar in the Streamlit application to select a subdirectory and then choose an HTML file to view its contents.

## Project Structure

- `convert_to_html.py` - Script to convert `.ipynb` files to HTML format.
- `app.py` - Streamlit application script for browsing and viewing HTML files.
- `Lectures/` - The directory for your source Jupyter Notebooks to be converted.
- `html/` - (Generated) The destination directory for resulting HTML files.

## Contributing

Contributions are welcome! Please feel free to submit a pull request, open an issue, or fork the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

