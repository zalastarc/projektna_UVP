import re
import requests

def prenesi_html(link):
    vzorec = requests.get(link)
    with open('html', 'w', encoding='utf8') as f:
        print(vzorec.text, file=f)


prenesi_html("https://zotks.si/priznanja/logika/")