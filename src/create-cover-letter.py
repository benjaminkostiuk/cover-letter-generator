import sys
from docx import Document
from docx2pdf import convert
from configuration import Configuration
import shutil
from pathlib import Path

USAGE = "Usage: python3 create-cover-letter.py <FILENAME>"
CONFIG_FILE = "config.json"

# Ensure the filename argument is passed or print help message
if len(sys.argv) != 2 or sys.argv[1].lower() == 'help':
    print(USAGE)
    exit(1)

# Create config
config = Configuration(CONFIG_FILE)
config.prompt_for_replacements()
config.copy_contact_and_defaults_to_replacements()

# Setup output artifact names
doc_name = f'{sys.argv[1]}CoverLetter.docx'
doc_path = Path(config.word_path).joinpath(doc_name).resolve()
pdf_name = f'{sys.argv[1]}CoverLetter.pdf'
pdf_path = Path(config.pdf_path).joinpath(pdf_name).resolve()

# Copy over from template
shutil.copyfile(config.template_path, doc_path)
# Create document
document = Document(doc_path)

# Replace in text
for paragraph in document.paragraphs:
    for key in config.replacements.keys():
        if key in paragraph.text:
            paragraph.text = paragraph.text.replace(key, config.replacements[key])

# Save document
document.save(doc_path)

# Generate pdf
convert(doc_path, pdf_path)
