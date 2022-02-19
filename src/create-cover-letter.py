import sys
from os.path import join
from docx import Document
from docx2pdf import convert
from datetime import date
from configuration import Configuration
import shutil
from pathlib import Path

USAGE = "Usage: python3 create-cover-letter.py <FILENAME>"
CONFIG_FILE = "config.json"

# Ensure the filename argument is passed
if len(sys.argv) != 2:
    print(USAGE)
    exit(1)

# Create config
config = Configuration(CONFIG_FILE)
config.prompt_for_replacements()

# Setup output artifact names
doc_name = f'{sys.argv[1]}CoverLetter.docx'
doc_path = Path(config.word_path).joinpath(doc_name).resolve()
pdf_name = f'{sys.argv[1]}CoverLetter.pdf'
pdf_path = Path(config.pdf_path).joinpath(pdf_name).resolve()

# Copy over from template
shutil.copyfile(config.template_path, doc_path)
# Create document
document = Document(doc_path)

# # Create dictionary of keys
# company_name = input("Enter name of company: ")
# position_name = input("Enter position name: ")

# print("Choose reason you like position:")
# print("[0] " + options[0])
# print("[1] " + options[1])
# print("[2] " + options[2])
# reason = int(input("Choice: "))

replacements = {
    # "<Company Name>": company_name,
    # "<Position Name>": position_name,
    # "<Reason>": options[reason],
    "<Date>": date.today().strftime("%A, %B %d, %Y")
}

# Replace in text
for paragraph in document.paragraphs:
    for key in replacements.keys():
        if key in paragraph.text:
            paragraph.text = paragraph.text.replace(key, replacements[key])

# Save document
document.save(doc_path)

# Generate pdf
convert(doc_path, pdf_path)
