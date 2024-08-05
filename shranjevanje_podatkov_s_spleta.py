import csv

from podatki_s_spleta import prenesi_html, izlusci_podatke, izlusci_podatke_iz_posameznega_bloka

def naredi_csv(datoteka):
    """Funkcija naredi csv datoteko z želenimi podatki."""
    with open(datoteka, 'w', encoding='utf8') as f:
        pisec = csv.writer(f)
        pisec.writerow(
            [
                'Skupina',
                'Tekmovalec',
                'Mentor',
                'Šola',
                'Točke',
                'Mesto'
            ]
        )
        html = prenesi_html('https://zotks.si/priznanja/logika/')
        bloki = izlusci_podatke(html)
        for blok in bloki:
            slovar = izlusci_podatke_iz_posameznega_bloka(blok)
            pisec.writerow(
                [
                    slovar['Skupina'],
                    slovar['Tekmovalec'],
                    slovar['Mentor'],
                    slovar['Šola'],
                    slovar['Točke'],
                    slovar['Mesto']
                ]
            )

naredi_csv('datoteka.csv')
