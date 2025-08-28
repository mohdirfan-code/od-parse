# `od-parse`-Powered Document Extractor

## Project Summary

This project is a resilient and simple command-line application that demonstrates the core document parsing and data extraction capabilities of the `od-parse` library. It is designed to take a multi-page PDF, intelligently process its content, and output the results as a human-readable Markdown file.

This project was developed as a submission for an application process at OctonData. It highlights not only the functionality of `od-parse` but also a methodical approach to software development, problem-solving, and delivering a functional product within constraints.

-----

## Features

  - **Intelligent Document Parsing**: Leverages `od-parse` to perform comprehensive extraction of text, tables, forms, and other data from PDF files.
  - **Robust Markdown Generation**: Converts the raw, structured output from the parser into a clean and well-formatted `sample_document.md` file.
  - **Simplified Dependency Stack**: Consciously designed to run without complex external dependencies like Java and large deep-learning models, ensuring a quick and seamless setup process.
  - **Resilient Codebase**: The Python script includes strategic patches and robust error handling to navigate known issues in the library, guaranteeing a stable execution environment.

-----

## Project Architecture

The project follows a straightforward pipeline to process a PDF document:

1.  **Parsing**: The `simple_parser.py` script calls the `od-parse` library to extract raw content from the PDF.
2.  **Conversion**: The extracted data is then passed to the `convert_to_markdown` utility.
3.  **Output**: A formatted Markdown file is generated, containing all the parsed content in a clear structure.

-----

## Setup and Installation

This guide assumes you have Python 3.8+ and Git installed on your system.

1.  **Clone the `od-parse` library and set up the project folder:**

    ```bash
    git clone https://github.com/octondata/od-parse.git
    # Now place your `simple_parser.py` and `sample_document.pdf` files here.
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    cd od-parse
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the core dependencies and the `od-parse` library itself:**

    ```bash
    pip install pdfminer.six pillow numpy pandas
    pip install -e .
    ```

4.  **Patch the `od-parse` library to fix a known bug**:
    Open the file `od_parse/converter/markdown_converter.py` and add the following code at the beginning of the `format_table` function (around line 125):

    ```python
    # FIX: Add a check for empty table data to prevent KeyErrors
    if not table_data:
        return ""
    ```

5.  **Navigate back to the root project folder:**

    ```bash
    cd ..
    ```

-----

## Usage

To run the project, ensure your virtual environment is active and execute the `simple_parser.py` script from the root directory.

```bash
# Activate the virtual environment
.\od-parse\venv\Scripts\activate

# Run the script
python simple_parser.py
```

Upon successful completion, a new file named **`sample_document.md`** will be created in the project's root folder, containing the extracted text and structured data.

-----
