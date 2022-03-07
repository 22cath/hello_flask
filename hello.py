# creando un servidor web con flask y una app para poder comunicarnos con el servidor
from flask import Flask

app = Flask(__name__)
@app.route("/")
def la_funcion():
    return "Hola, Flask!"

@app.route("/bye/<nombre>")
def otra_funcion(nombre):
    return f"hasta luego {nombre}"

