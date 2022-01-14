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
    if kontonummer in range(1, 4): # stellt sicher, dass eine gültige kontonummer eingegeben wurde
        str.kontonummer = str(kontonummer) # der int kontonummer wird in einen string umgewandelt, damit er mit dem anderen string "konto" zusammengefügt werden kann
        konto = 'konto' + str.kontonummer # die beiden strings werden zusammengefügt um den variablen namen der verschiedenen kontos zu generieren
        globals()[konto] = globals()[konto] + betrag # mit der funktion globals()[konto] wird auf die globalen variablen kont1, konto2 usw. zugegriffen
                                                     # der alte kontostand wird mit dem gewünschten betrag a verrechnet
        print (globals()[konto])
    else:
        print ("Kein existierendes Konto ausgewählt.") # falls eine zahl eingegeben wird, welcche nicht einem konto entspricht erscheint dieser text, dadurch können fehlermeldungen vermieden werden.


def uebertragen (kontonummer_von, kontonummer_zu, betrag): # funktion zum übertragen von beträgen
    if kontonummer_von in range (1, 4) and kontonummer_zu in range (1, 4): # stellt sicher, dass eine gültige kontonummer eingegeben wird
        str_kontonummer_von = str(kontonummer_von) # int wird in string umgewandelt
        str_kontonummer_zu = str(kontonummer_zu) # =
        konto_von = 'konto' + str_kontonummer_von # variablennamen werden zusammengesetzt
        konto_zu = 'konto' + str_kontonummer_zu # =
        globals()[konto_von] = globals()[konto_von] - betrag # betrag wird vom ausgangskonto subtrahiert
        globals()[konto_zu] = globals()[konto_zu] + betrag # betrag wird zum eingangskonto addiert
        print ("Der Kontostand von " + str(konto_von) + " ist neu " + str(globals()[konto_von])) # neuer kontostand vom ausgangskonto wird ausgegeben
        print ("Der Kontostand voon " + str(konto_zu) + " ist neu " + str(globals()[konto_zu])) # neuer kontostand vom eingangskonto wird ausgegeben
    else:
        print ("Eines oder beide der ausgewählten Konten existieren nicht.") # wurde eine kontonummer ausgewählt, welches niccht exisitert wird dieser text ausgegeben, dadurch werden fehlermeldungen vermieden


def kontostand (kontonummer): # funktion zum kontostand
    if kontonummer in range(1, 4): # stellt sicher, dass eine existtierende kontonummer eingegeben wird
        str_kontonummer = str(kontonummer) # int wird in string umgewandelt
        konto = 'konto' + str_kontonummer # variablen werden zusammengesetzt
        print (globals()[konto]) # kontostand wird ausgegeben
    else:
        print ("Kein existierendes Konto ausgewählt.") # erscheint wenn eine nicht existierende kontonummer eingegeben wurde, dadurch werden fehlermeldunngen vermiedens