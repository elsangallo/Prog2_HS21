from flask import Flask # flask wird aus dem package flask importiert
from flask import render_template # die funktion render_template wird importiert
from flask import request # die funktion request wird importiert

# kontos werden als einfache variablen kreiert. jedes konto ist eine eigene variable mit kontostand 0.
konto1 = 0
konto2 = 0
konto3 = 0
konto4 = 0

#runs on http://localhost:5001/bank
app = Flask("Bankkonto") # die flask-app "Bankkonto" wird erstellt


@app.route('/bank') # der url-link für die app wird erstellt, die url mit der endung "bank" führt dann die untenstehende funktion aus
def bank(): # die funktion bank() führt die funktion render_template aus, womit das html-template ausgeführt wird, welches im file index.html erstellt wurde
    return render_template('index.html', name="Elias") # im index.html wird der wert für die variable nicht festgelegt, dass wird hier mit name="Elias" gemacht, dadurch lässt es sich leichter anpassen


@app.route('/bank/ein_auszahlen', methods=['GET', 'POST']) # die url ein_auszahlen wird erstellt
def ein_auszahlen(): # die funktion der url wird erstellt, wenn man draufklickt erscheinnt der untenstehende text
    if request.method == 'POST': # falls mit der methode post etwas von der webseite ausgegeben wird werden nachfolgende zeilen ausgeführt
        kontonummer = request.form['kontonummer'] # die kontonummer wird aus dem formularfeld kontonummer abgefragt und als variable kontonummer gespeichert
        betrag = int(request.form['betrag']) # der betrag wird aus dem formularfeld betrag abgefragt
        konto = 'konto' + kontonummer # variable konto wird mit dem wort konto und der eingegebenen kontonummer gefüllt
        globals()[konto] = globals()[konto] + betrag # der neue kontostand wird berechnet indem die globale variable aufgerufen wird
        return 'Der neue Kontostand von ' + konto + ' ist jetzt ' + str(globals()[konto]) # der neue kontostand wird ausgegeben
    else:
        return render_template('ein_auszahlen.html') # das template ein-auszahlen wird aufgerufen


@app.route("/bank/uebertragen", methods=['GET', 'POST']) # die url übertragen wird erstellt
def uebertragen(): # die funktion der url wird erstellt, wenn man draufklickt erscheint der untenstehende text
    if request.method == 'POST': # falls mit der methode post etwas von der webseite ausgegeben wird werden nachfolgende zeilen ausgeführt
        kontonummer_von = request.form['kontonummer_von'] # die kontonummer des belastungskontos wird aus dem formularfeld kontonummer_von abgefragt und als variable kontonummer_von gespeichert
        kontonummer_zu = request.form['kontonummer_zu'] # die kontonummer des empfängerkontos wird aus dem formularfeld kontonummer_zu abgefragt und als variable kontonummer_zu gespeichert
        betrag = int(request.form['betrag']) # der betrag wird aus dem formularfeld betrag abgefragt
        konto_von = 'konto' + kontonummer_von  # variable konto_von wird mit dem wort konto und der eingegebenen kontonummer des belastungskontos gefüllt
        konto_zu = 'konto' + kontonummer_zu # variable konto_zu wird mit dem wort konto und der eingegebenen kontonummer des empfängerkontos gefüllt
        globals()[konto_von] = globals()[konto_von] - betrag # der neue kontostand wird berechnet indem die globale variable aufgerufen wird
        globals()[konto_zu] = globals()[konto_zu] + betrag # der neue kontostand wird berechnet indem die globale variable aufgerufen wird
        answer1 = 'Der Kontostand von ' + konto_von + ' ist neu ' + str(globals()[konto_von]) # die variable answer1 wird mit einem satz und der variable konto_von gefüllt zuzüglich wird die globale varibale abgerufen unnd eingefügt
        answer2 = 'Der Kontostand von ' + konto_zu + ' ist neu ' + str(globals()[konto_zu]) # die variable answer2 wird mit einem satz und der variable konto_zu gefüllt zuzüglich wird die globale varibale abgerufen unnd eingefügt
        return answer1 + '. ' + answer2 # die variable answer1 und answer2 werden zusammengefügt und ausgegeben
    else:
        return render_template('uebertragen.html') # das template üebertragen wird abgerufen


@app.route("/bank/kontostand", methods=['GET', 'POST']) # die url kontostand wird erstellt
def kontostand(): # die funktion der url wird erstellt, wenn man draufklickt erscheint der untenstehende text
    if request.method == 'POST': # falls mit der methode post etwas von der webseite ausgegeben wird werden nachfolgende zeilen ausgeführt
        kontonummer = request.form['kontonummer'] # die kontonummer wird aus dem formularfeld kontonummer abgefragt und als variable kontonummer gespeichert
        konto = 'konto' + kontonummer # variable konto wird mit dem wort konto und der eingegebenen kontonummer gefüllt
        return str(globals()[konto]) # die globale variable wird ausgegeben
    else:
        return render_template('kontostand.html') # das template kontostand wird abgerufen

if __name__ == "__main__":
    app.run(debug=True, port=5001) # hiermit wird festgelegt, dass wenn die app startet das debugging ein und der port 5001 abgerufen wird