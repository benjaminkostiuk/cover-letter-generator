
from pathlib import Path
from datetime import date, datetime
import json

# Path to root of the project
ROOT_DIR = Path(__file__).parent.parent

'''
    Configuration Object
'''
class Configuration:
    # Resolve a path given in the config file
    # Gives preference to the full path over the relative path
    def __resolve_path(path, rel_path):
        return Path(path).resolve() if path else ROOT_DIR.joinpath(rel_path).resolve()

    # Build a dictionary of the contact information
    def __build_contact(contact):
        return { contact[name]['tag']: contact[name]['value'] for name in contact }

    # Build a dictionary of the default values passed to the template
    def __build_defaults():
        return {
            "<DATE>": date.today().strftime("%A, %B %d, %Y"),
            "<TIMESTAMP>": datetime.now().strftime("%d-%m-%YT%H:%M:%S")
        }

    def __init__(self, config_file_name):
        # Read config json
        CONFIG_FILE = ROOT_DIR.joinpath(config_file_name).resolve()
        with open(CONFIG_FILE, 'r') as f:
            data = json.load(f);

        # Set paths
        self.template_path = Configuration.__resolve_path(data['templateFullPath'], data['templatePath'])
        self.word_path = Configuration.__resolve_path(data['wordDirFullPath'], data['wordDirPath'])
        self.pdf_path = Configuration.__resolve_path(data['pdfDirFullPath'], data['pdfDirPath'])

        # Build contact
        self.contact = Configuration.__build_contact(data['contact'])
        # Save body data
        self.body = data['body']
        # Build defaults
        self.defaults = Configuration.__build_defaults()
        # Set replacementas as empty dict
        self.replacements = dict()

    # Prompt user for data to build body replacements
    def prompt_for_replacements(self):
        for replacement in self.body:
            # Set user prompt to prompt or tag name
            prompt = replacement['prompt'] if replacement['prompt'] else replacement['tag']
            if replacement['type'] == 'input':
                self.replacements[replacement['tag']] = input(f'{prompt}: ')
            
            elif replacement['type'] == 'choice':
                print(prompt)
                # Print out each choice with their index
                for i, choice in enumerate(replacement['choice']):
                    print(f'[{i}] {choice}')
                chosen = input("Choice: ")
                self.replacements[replacement['tag']] = replacement['choice'][int(chosen)]

    # Copy over contact replacements and defaults to replacements
    def copy_contact_and_defaults_to_replacements(self):
        for c in self.contact:
            self.replacements[c] = self.contact[c]
        for d in self.defaults:
            self.replacements[d] = self.defaults[d]
