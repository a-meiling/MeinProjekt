#----------------------------
# Dateiname: teilprüfung6_GUI.py
# Autor: Anne Meiling
# Letzte Änderung: 15.01.2025
# Das ist die zweite Änderung für die Git-Teilprüfung
#----------------------------

class Buch:
    def __init__(self, titel, autor, kategorie, preis):
        self.titel = titel
        self.autor = autor
        self.kategorie = kategorie
        self.preis = preis

    def __str__(self):
        return f'{self.titel} ({self.kategorie}) von {self.autor} für {self.preis}€'
        

class Buchladen:
    def __init__(self):
        self.inventar = []
        self.auswahl = []

    def buch_hinzufügen(self, titel, autor, kategorie, preis):
        neues_buch = Buch(titel, autor, kategorie, float(preis))
        self.inventar.append(neues_buch)

    def inventar_durchsuchen(self, kategorie):
        print(f'Kategorie "{kategorie}" enthält folgende Bücher:')
        gefundene_bücher=[b for b in self.inventar if b.kategorie.lower() == kategorie.lower()]
        if gefundene_bücher:
            for buch in gefundene_bücher:
                print(f'-{buch.titel} von {buch.autor}')
        else:
            print('Keine Bücher in der Kategorie gefunden.')

    def buch_zur_auswahl(self, titel):
        for b in self.inventar:
            if b.titel.lower() == titel.lower():
                self.auswahl.append(b)
                return
        print('Es wurde kein Buch mit diesem Titel gefunden.')

    def gesamtpreis_berechnen(self):
        auswahl_preise = [b.preis for b in self.auswahl]
        gesamtpreis = sum(auswahl_preise)
        return gesamtpreis


def main():
    MENU='''
Wählen Sie eine Aktion:

a) Buch dem Inventar hinzufügen
b) Inventar durchsuchen
c) Gesamtpreis einer Auswahl berechnen
d) Programm beenden    
'''
    bl = Buchladen()
    
    bl.buch_hinzufügen('Die Mitternachtsbibliothek','Matt Haig','Roman',12.99)
    bl.buch_hinzufügen('Powerful - Building a Culture of Freedom and Responsibility',
                       'Patty McCord', 'Sach-& Fachbücher', 26.99)
    bl.buch_hinzufügen('Mindset - Changing the way you think to fulfil your potential',
                       'Dr Carol S. Dweck', 'Sach-& Fachbücher', 12.99)
    bl.buch_hinzufügen('Nähen - Schritt für Schritt', 'Alison Smith', 'Sach-& Fachbücher',16.95)
    bl.buch_hinzufügen('Designing Games - A guide to engeneering experiences',
                       'Tynan Sylvester', 'Sach-&Fachbücher', 43.99)

    while True:
        print(MENU)
        eingabe = (input('Auswahl: ')).strip().lower()
              
        if eingabe == 'd':
            print('Programm wird beendet.')
            break

        elif eingabe == 'a':
            titel = input('Titel: ')
            autor = input('Autor: ')
            kategorie = input('Kategorie: ')
            preis = input('Preis: ')
            bl.buch_hinzufügen(titel, autor, kategorie, preis)
            print(f'\nDas Buch "{titel}" wurde dem Inventar hinzugefügt.')
                    
        elif eingabe == 'b':
            kategorie = (input('Suchbegriff (Kategorie): '))
            bl.inventar_durchsuchen(kategorie)

        elif eingabe == 'c':
            auswahl = 'ja'
            while auswahl == 'ja':
                titel = (input('Buchtitel: '))
                bl.buch_zur_auswahl(titel)
                auswahl = (input('Ein weiteres Buch hinzufügen? (ja/nein): ')).strip().lower()
            gesamtpreis = bl.gesamtpreis_berechnen()
            print(f'\nDer Gesamtpreis der Bücher \n{"\n".join([b.titel for b in bl.auswahl])} \nbeträgt {round(gesamtpreis,2)}€')

        else:
            print('Eingabe wurde nicht erkannt. Bitte nutzen Sie eine der vorgegebenen Optionen.')

if __name__ == '__main__':
    main()
