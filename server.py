from flask import Flask, jsonify, request
from logica import Biblioteca
app = Flask(__name__)

biblioteca = Biblioteca()

@app.route("/")
def index():
    return "Hola desde flask"

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
    app.run(debug=True)

