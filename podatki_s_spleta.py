import re
import requests

def prenesi_html(link):
    vzorec = requests.get(link)
    #with open('html', 'w', encoding='utf8') as f:
    #    print(vzorec.text, file=f)
    return vzorec.text

# prenesi_html("https://zotks.si/priznanja/logika/")


def izlusci_podatke(niz):
    vzorec = r'<td data-label="Skupina">.*?</tr>'
    return re.findall(vzorec, niz, flags=re.DOTALL)

print(len(izlusci_podatke(prenesi_html("https://zotks.si/priznanja/logika/"))))

def izlusci_podatke_iz_posameznega_bloka(blok):
    vzorec = re.compile(
        r'<td data-label="Skupina">(?P<Skupina>.*?)</td>.*?'
        r'<td data-label="Tekmovalec">(?P<Tekmovalec>.*?)</td>.*?'
        r'<td data-label="Mentor">(?P<Mentor>.*?)</td>.*?'
        r'<td data-label="Šola">(?P<Šola>.*?)</td>.*?'
        r'<td data-label="Točke">(?P<Točke>.*?)</td>.*?'
        r'<td data-label="Mesto">(?P<Mesto>.*?)</td>',
        re.DOTALL)
    najdbe = vzorec.search(blok)
    print(najdbe['Skupina'])


izlusci_podatke_iz_posameznega_bloka((izlusci_podatke(prenesi_html("https://zotks.si/priznanja/logika/")))[0])
