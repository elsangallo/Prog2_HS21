from flask import Flask # flask wird aus dem package flask importiert
from flask import render_template # die funktion render_template wird importiert
from flask import request

# kontos werden als einfache variablen kreiert. jedes konto ist eine eigene variable mit kontostand 0.
Konto1 = 500
Konto2 = 200
Konto3 = 0
Konto4 = 0

#runs on http://localhost:5001/bank
app = Flask("Bankkonto") # die flask-app "Bankkonto" wird erstellt


@app.route('/bank') # der url-link für die app wird erstellt, die url mit der endung "bank" führt dann die untenstehende funktion aus
def bank(): # die funktion bank() führt die funktion render_template aus, womit das html-template ausgeführt wird, welches im file index.html erstellt wurde
    return render_template('index.html', name="Elias") # im index.html wird der wert für die variable nicht festgelegt, dass wird hier mit name="Elias" gemacht, dadurch lässt es sich leichter anpassen


@app.route('/bank/ein_auszahlen', methods=['GET', 'POST']) # die url ein_ausbezahlen wird erstellt
def ein_auszahlen(): # die funktion der url wird erstellt, wenn man draufklickt ersccheinnt der untenstehende text
    if request.method == 'POST':
        kontonummer = request.form['kontonummer']
        betrag = int(request.form['betrag'])
        konto = 'konto' + kontonummer
        globals()[konto] = globals()[konto] + betrag
        return 'Der neue Kontostand von ' + konto + ' ist jetzt ' + str(globals()[konto])
    else:
        return render_template('ein_auszahlen.html')


@app.route("/bank/uebertragen", methods=['GET', 'POST']) # die url übertragen wird erstellt
def uebertragen(): # die funktion der url wird erstellt, wenn man draufklickt erscheint der untenstehende text
    if request.metthod == 'POST':
        kontonummer_von = request.form['kontonummer_von']
        kontonummer_zu = request.form['kontonummer_zu']
        betrag = int(request.form['betrag'])
        konto_von = 'konto' + kontonummer_von
        konto_zu = 'konto' + kontonummer_zu
        globals()[konto_von] = globals()[konto_von] - betrag
        globals()[konto_zu] = globals()[konto_zu] + betrag
        answer1 = 'Der Kontostand von ' + konto_von + ' ist neu ' + str(globals()[konto_von])
        answer2 = 'Der Kontostand von ' + konto_zu + ' ist neu ' + str(globals()[konto_zu])
        return answer1 + answer2
    else
        return render_template('uebertragen.html')


@app.route("/kontostand") # die url kontostand wird erstellt
def kontostand(): # die funktion der url wird erstellt, wenn man draufklickt erscheint der untenstehende text
    return "Dein Kontostand ist: "


if __name__ == "__main__":
    app.run(debug=True, port=5001) # hiermit wird festgelegt, dass wenn die app startet das debugging ein und der port 5001 abgerufen wird