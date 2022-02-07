import sys
from os.path import join
from docx import Document
from docx2pdf import convert
from datetime import date

WORD_DIR="D:\\OneDrive\\Documents\\University\\Resume and Co-op\\Cover Letters\\Word"
PDF_DIR="D:\\OneDrive\\Documents\\University\\Resume and Co-op\\Cover Letters\\PDFs"

options = ["intern growth and development", "developing for the future", "hands-on development and making an impact"]

# Usage
# python modify-cover-letter.py FILENAME
if len(sys.argv) != 2:
    print("Usage: python modify-cover-letter.py FILENAME")
    exit(1)

# Get document
docName = sys.argv[1]
pdfName = docName.replace(".docx", ".pdf")
document = Document(docName)

# Create dictionary of keys
company_name = input("Enter name of company: ")
position_name = input("Enter position name: ")

print("Choose reason you like position:")
print("[0] " + options[0])
print("[1] " + options[1])
print("[2] " + options[2])
reason = int(input("Choice: "))

replacements = {
    "<Company Name>": company_name,
    "<Position Name>": position_name,
    "<Reason>": options[reason],
    "<Date>": date.today().strftime("%A, %B %d, %Y")
}

# Replace in text
for paragraph in document.paragraphs:
    for key in replacements.keys():
        if key in paragraph.text:
            paragraph.text = paragraph.text.replace(key, replacements[key])
# Save document
document.save(docName)

# Generate pdf
convert(join(WORD_DIR, docName), join(PDF_DIR, pdfName))
