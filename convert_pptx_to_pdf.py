import os
import subprocess
import json

def load_config(config_file="config.json"):
    with open(config_file, "r") as file:
        return json.load(file)

def convert_pptx_to_pdf(input_folder, output_folder):
    """ Converts all PPTX files in input_folder to PDFs in output_folder """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pptx_files = [f for f in os.listdir(input_folder) if f.endswith('.pptx')]

    if not pptx_files:
        print("No PPTX files found in the folder.")
        return

    libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"

    for pptx in pptx_files:
        input_path = os.path.join(input_folder, pptx)
        output_path = os.path.join(output_folder, pptx.replace('.pptx', '.pdf'))
        
        # Convert using LibreOffice
        try:
            subprocess.run([libreoffice_path, "--headless", "--convert-to", "pdf", "--outdir", output_folder, input_path], check=True)
            print(f"Converted: {pptx} -> {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {pptx}: {e}")

if __name__ == "__main__":
    config = load_config()
    input_dir = config.get("input_folder")
    output_dir = config.get("output_folder")
    convert_pptx_to_pdf(input_dir, output_dir)
