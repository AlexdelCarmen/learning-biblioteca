from flask import Flask, jsonify, request, send_from_directory
from logica import Biblioteca
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)

biblioteca = Biblioteca()

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/libros", methods=["GET"])
def index_libros():
    return jsonify(biblioteca.obtener_libros())

@app.route("/libros/autor/<autor>")
def buscar_autor(autor):
    return jsonify(biblioteca.buscar_por_autor(autor))

@app.route("/libros/titulo/<titulo>")
def buscar_titulo(titulo):
    return jsonify(biblioteca.buscar_por_titulo(titulo))

@app.route("/libros", methods=["POST"])
def agregar_libro(): 
    try:
        datos = request.get_json()
        biblioteca.agregar_libro(
            datos["titulo"],
            datos["autor"],
            datos["año"],
            datos["genero"]
        )
        return jsonify({"mensaje": "Libro agregado con exito"}), 201
    except: 
        return jsonify({"mensaje": "Datos incompletos"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

