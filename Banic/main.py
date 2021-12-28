# Grundlegende Variante (nur Python)

# Konten werden als einfache Variablen kreiert. Jedes Konto ist eine eigene Variable mit dem Kontostand=0.
Konto1 = 500
Konto2 = 200
Konto3 = 0
Konto4 = 0

# 1. Funktion: ein- und auszahlen auf ein bestimmtes Konto und anschliessendes Anzeigen des Kontostands.
# Parameter kontonummer zeigt an, für welches Konto die Ein-/Auszahlung getätigt werden soll.
# Parameter a gibt an, wei viel ein- bzw. ausbezahlt werden soll.
# Idee von: https://www.pythonpool.com/python-string-to-variable-name/
def ein_auszahlen (kontonummer, betrag):
    if kontonummer in range(1, 4):
        str.kontonummer = str(kontonummer) # der int kontonummer wird in einen string umgewandelt, damit er mit dem anderen string "konto" zusammengefügt werden kann
        konto = 'konto' + str.kontonummer # die beiden strings werden zusammengefügt um den variablen namen der verschiedenen kontos zu generieren
        globals()[konto] = globals()[konto] + betrag # mit der funktion globals()[konto] wird auf die globalen variablen kont1, konto2 usw. zugegriffen
                                                     # der alte kontostand wird mit dem gewünschten betrag a verrechnet
        print (globals()[konto])
    else:
        print ("Kein existierendes Konto ausgewählt.")


def uebertragen (kontonummer_von, kontonummer_zu, betrag):
    if kontonummer_von in range (1, 4) and kontonummer_zu in range (1, 4):
        str_kontonummer_von = str(kontonummer_von)
        str_kontonummer_zu = str(kontonummer_zu)
        konto_von = 'konto' + str_kontonummer_von
        konto_zu = 'konto' + str_kontonummer_zu
        globals()[konto_von] = globals()[konto_von] - betrag
        globals()[konto_zu] = globals()[konto_zu] + betrag
        print ("Der Kontostand von " + str(konto_von) + " ist neu " + str(globals()[konto_von]))
        print ("Der Kontostand voon " + str(konto_zu) + " ist neu " + str(globals()[konto_zu]))
    else:
        print ("Eines oder beide der ausgewählten Konten existieren nicht.")


def kontostand (kontonummer):
    if kontonummer in range(1, 4):
        str_kontonummer = str(kontonummer)
        konto = 'konto' + str_kontonummer
        print (globals()[konto])
    else:
        print ("Kein existierendes Konto ausgewählt.")