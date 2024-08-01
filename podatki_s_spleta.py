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

# print(len(izlusci_podatke(prenesi_html("https://zotks.si/priznanja/logika/"))))

def izlusci_podatke_iz_posameznega_bloka(blok):
    slovar = {}
    vzorec = re.compile(
        r'<td data-label="(s||S)kupina">(?P<Skupina>.*?)</td>.*?'
        r'<td data-label="(t||T)ekmovalec">(?P<Tekmovalec>.*?)</td>.*?'
        r'<td data-label="(m||M)entor">(?P<Mentor>.*?)</td>.*?'
        r'<td data-label="(š||Š)ola">(?P<Šola>.*?)</td>.*?'
        r'<td data-label="(t||T)očke">(?P<Točke>.*?)</td>.*?'
        r'<td data-label="(m||M)esto">(?P<Mesto>.*?)</td>',
        re.DOTALL)
    najdbe = vzorec.search(blok)
    # print(najdbe['Skupina'])
    slovar['Skupina'] = najdbe['Skupina']
    slovar['Tekmovalec'] = najdbe['Tekmovalec']
    slovar['Mentor'] = najdbe['Mentor']
    slovar['Šola'] = najdbe['Šola']
    slovar['Točke'] = najdbe['Točke']
    slovar['Mesto'] = najdbe['Mesto']
    return slovar



# print(izlusci_podatke_iz_posameznega_bloka((izlusci_podatke(prenesi_html("https://zotks.si/priznanja/logika/")))[0]))
