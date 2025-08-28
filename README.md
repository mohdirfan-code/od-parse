````markdown
# Simple Document Text Extractor using `od-parse`

## Project Summary

This project is a simple command-line application that demonstrates the core functionality of the `od-parse` library for document processing. It is designed to parse a multi-page PDF document, extract its text and structured data, and convert the output into a clean, human-readable Markdown format.

The project was created as part of an application process for OctonData.

## Features

- **Document Parsing**: Utilizes `od-parse` to extract text from a PDF.
- **Markdown Conversion**: Transforms the structured output from `od-parse` into a formatted Markdown file (`sample_document.md`).
- **Simplified Dependency Stack**: This project has been optimized to run without complex external dependencies like Java and deep learning models to ensure a quick and seamless setup.
- **Robust Code**: The Python script includes error handling and path management to provide a stable execution environment.

## Installation

This guide assumes you have Python 3.8+ and `git` installed.

1.  **Clone the `od-parse` library and set up the project structure:**
    ```bash
    git clone [https://github.com/octondata/od-parse.git](https://github.com/octondata/od-parse.git)
    ```

2.  **Navigate into the cloned directory and create a virtual environment:**
    ```bash
    cd od-parse
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the necessary dependencies:**
    ```bash
    pip install pdfminer.six pillow numpy pandas
    pip install -e .
    ```

4.  **Place the `sample_document.pdf` and `simple_parser.py` files in the root project directory.**
    ```bash
    cd ..
    ```

## Usage

To run the project, ensure your virtual environment is active and execute the `simple_parser.py` script from the root directory.

```bash
# Activate the virtual environment
.\od-parse\venv\Scripts\activate

# Run the script
python simple_parser.py
````

Upon successful completion, a new file named `sample_document.md` will be created, containing the extracted text content.


