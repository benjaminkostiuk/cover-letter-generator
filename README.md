# Cover Letter Generator
Quickly generate cover letters using mad lib style completions to speed up your application process. Built for Windows.

## How it works
[[Demo]](https://youtu.be/rByzDIo1LlU)

The script uses a simple find-and-replace algorithm to replace all tags found in the [template file](./CoverLetterTemplate.docx), as specified by the [configuration file](./config.json) with values given by the user. The new word file with all the replacements is saved along with a .pdf version in separate directories.

## Setup
- Install [Python 3](https://www.python.org/downloads/)
- Install [pip](https://pip.pypa.io/en/stable/installation/)
- Clone this repo
```shell
git clone https://github.com/benjaminkostiuk/cover-letter-generator.git
```
- (Optionally) create a python virtual environment
- Install required dependencies
```shell
pip install -r requirements.txt
```
### Update template
- Open the [CoverLetterTemplate.docx](./CoverLetterTemplate.docx) word document and update the template to your preferences. A default template is provided.

- All replacements **will only occur in the body of the document** this means that you cannot use tags in the header or footer of the document. Only the body's paragraphs will be searched.

- The [python-docx](https://python-docx.readthedocs.io/en/latest/) package will use the **default font** and formatting in Word when making replacement so you must set the Default Font _before_ running the script. You can do this by expanding the Font settings, selecting the font you want and clicking _Set As Default_.

### Update config.json
- Open the [config.json](./config.json) file and update it with the following:
    - Update the paths where you want the generated word and pdf documents to be saved.
        - By default they are saved in the `word` and `pdf` directories.
        - You can either set the full path or the relative path to the word or pdf folders. The full path will take precedence if both are specified.
    - Update your contact information tags as necessary.
    - Add any additional tags and their values.
        - Each tag must be unique for the search and replace algorithm to be effective.
        - When defining replacements up you can either choose between `input` and `choice` types.
        - The default tags `<DATE>` and `<TIMESTAMP>` are provided for you.


### Add shell script to path or as alias
For quick and easy access to your script you can either add this project directory to your path. (Change the path to this project in the below command)
```shell
echo 'export PATH=$PATH:C:\\path\\to\\this\\project\\cover-letter-generator' >> ~/.bash_profile
source ~/.bash_profile
```
Or add the following alias:
```shell
alias ccl='C:\\path\\to\\this\\project\\cover-letter-generator\\ccl.sh'
```

## Generating a cover letter

Generate a new cover letter based on your template by running
```shell
ccl <FILENAME>
```
Once, you've completed the prompts, this will generate 2 files:
- `<FILENAME>CoverLetter.docx` in the word output directory
- `<FILENAME>CoverLetter.pdf` in the pdf output directory 
