#!/bin/bash

# Shell script for windows to generate new resume pdf
# Source directory, must contain CoverLetterTemplate.docx
src='D:\OneDrive\Documents\University\Resume and Co-op\Cover Letters\Word'
# Directory where we store word documents
wordDir='D:\OneDrive\Documents\University\Resume and Co-op\Cover Letters\Word'
# Directorty where we store pdf documents
pdfDir='D:\OneDrive\Documents\University\Resume and Co-op\Cover Letters\PDFs'
p=`pwd`

cd 'D:\OneDrive\Documents\University\Resume and Co-op\Cover Letters\Word'
cp 'CoverLetterTemplate.docx' "$1CoverLetter.docx"

python 'D:\Projects\scripts\modify-cover-letter.py' "$1CoverLetter.docx"

cd $p