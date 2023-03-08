import importlib
from lang import choise as lang

def download_lang_packet()
    global lang_packet

with open('client.properties', 'r') as properties:
    while True:
        command = input(lang.main(str(properties.readline()[:-1]))['system']['login']['questions']['ConfirmLang'][0] + str(properties.readline()) + lang.main(str(properties.readline()))['system']['login']['questions']['ConfirmLang'][0])
        if command in True_aliases:
            print('Язык ')