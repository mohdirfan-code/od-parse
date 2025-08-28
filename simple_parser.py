import os
import sys
import json

# Add od-parse to the system path to find the module
sys.path.append(os.path.join(os.getcwd(), 'od-parse'))

from od_parse import parse_pdf, convert_to_markdown

def run_simple_parser(file_path: str):
    """
    Parses a PDF document using the core od-parse function and
    converts the result to Markdown.
    """
    print("🚀 Starting simple document parsing...")
    
    # --- 1. Parse the document using the core function ---
    print(f"📄 Parsing document: {file_path}")
    try:
        # This will use deep learning to extract text and other features
        # It may trigger a download of models on the first run
        # Tables are still disabled to avoid the Java dependency
        parsed_data = parse_pdf(file_path, use_deep_learning=True, extract_tables=False)
        print("✅ Parsing completed successfully!")
    except Exception as e:
        print(f"❌ An error occurred during parsing: {e}")
        return

    # --- 2. Convert the parsed data to Markdown ---
    print("🔄 Converting parsed data to Markdown...")
    markdown_content = convert_to_markdown(parsed_data)
    
    # --- 3. Save the Markdown to a file ---
    output_filename = os.path.splitext(os.path.basename(file_path))[0] + ".md"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print(f"🎉 Document content successfully saved to '{output_filename}'")
    
    # --- 4. Print the full JSON output for verification ---
    # This directly accesses the output and ensures we see everything
    print("\n--- Full JSON Output for Verification ---")
    print(json.dumps(parsed_data, indent=2))
    print("----------------------------------------")

    # --- 5. Print a summary of the extracted text from the document info ---
    text_content = parsed_data.get('parsed_data', {}).get('document_info', {}).get('full_text', 'No text content found.')
    print("\n--- Summary of Extracted Text (from Document Info) ---")
    print(text_content)
    print("-----------------------------------------------------")


if __name__ == "__main__":
    # Ensure the sample document is in this folder
    document_path = os.path.join(os.getcwd(), "sample_document.pdf")
    
    if not os.path.exists(document_path):
        print(f"❌ Error: The file '{document_path}' was not found.")
        print("Please ensure you've copied 'sample_document.pdf' to this directory.")
    else:
        run_simple_parser(document_path)