import json
from cryptography.fernet import Fernet

def main(lang):
    with open(lang + '.json', 'r') as lang_file_data:
        return json.load(lang_file_data)
