from flask import Flask, render_template, request
from modelo import Depreciacion

app = Flask(__name__)

@app.route("/", methods=["GET"])
def renderTemplate():
    return render_template("index.html")

@app.route("/valorMaquinaria", methods=["POST"])
def valorMaquinaria():
    valorMaquinariaDato = float(request.form["valorMaquinaria"])
    valorDesechoDato = float(request.form["valorDesecho"])
    valorVidaUtilDato = float(request.form["valorVidaUtil"])

    datos = Depreciacion(valorMaquinariaDato, valorDesechoDato, valorVidaUtilDato)

    calc = datos.calcularDepreciacionAnual()

    return render_template("index.html", depreciacion=calc)

if __name__ == "__main__":
    app.run(debug=True)
