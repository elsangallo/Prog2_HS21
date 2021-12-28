from flask import Flask # flask wird aus dem package flask importiert
from flask import render_template # die funktion render_template wird importiert

#runs on http://localhost:5001/bank
app = Flask("Bankkonto") # die flask-app "Bankkonto" wird erstellt


@app.route('/bank') # der url-link für die app wird erstellt, die url mit der endung "bank" führt dann die untenstehende funktion aus
def bank(): # die funktion bank() führt die funktion render_template aus, womit das html-template ausgeführt wird, welches im file index.html erstellt wurde
    return render_template('index.html', name="Elias") # im index.html wird der wert für die variable nicht festgelegt, dass wird hier mit name="Elias" gemacht, dadurch lässt es sich leichter anpassen


@app.route('/ein_auszahlen') # die url ein_ausbezahlen wird erstellt
def ein_auszahlen(): # die funktion der url wird erstellt, wenn man draufklickt ersccheinnt der untenstehende text
    return "Wie viel Geld möchtest du ein- oder auszahlen?"


@app.route("/uebertragen") # die url übertragen wird erstellt
def uebertragen(): # die funktion der url wird erstellt, wenn man draufklickt erscheint der untenstehende text
    return "Wie viel Geld möchtest du übertragen?"


@app.route("/kontostand") # die url kontostand wird erstellt
def kontostand(): # die funktion der url wird erstellt, wenn man draufklickt erscheint der untenstehende text
    return "Dein Kontostand ist: "


if __name__ == "__main__":
    app.run(debug=true, port=5001) # hiermit wird festgelegt, dass wenn die app startet das debugging ein und der port 5001 abgerufen wird