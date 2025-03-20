import os
import json
import fitz


def load_config(config_file="config.json"):
    with open(config_file, "r") as file:
        return json.load(file)

def merge_pdfs(input_folder, output_file="merged.pdf"):
    pdf_files = sorted([f for f in os.listdir(input_folder) if f.endswith(".pdf")])
    
    if not pdf_files:
        print("No PDF files found in the folder.")
        return

    merged_pdf = fitz.open()
    
    for pdf in pdf_files:
        pdf_path = os.path.join(input_folder, pdf)
        doc = fitz.open(pdf_path)
        merged_pdf.insert_pdf(doc)
        print(f"Added: {pdf}")

    merged_pdf.save(output_file)
    merged_pdf.close()
    print(f"\n✅ Merged PDF saved as: {output_file}")

if __name__ == "__main__":
    config = load_config()
    input_dir = config.get("output_folder")
    output_dir = config.get("output_file")
    merge_pdfs(input_dir,output_dir)
