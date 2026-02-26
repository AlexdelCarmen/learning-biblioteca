from flask import Flask, jsonify
from logica import Biblioteca
app = Flask(__name__)

biblioteca = Biblioteca()

@app.route("/")
def index():
    return "Hola desde flask"

@app.route("/libros")
def index_libros():
    return jsonify(biblioteca.libros)

@app.route("/libros/autor/<autor>")
def buscar_autor(autor):
    return jsonify(biblioteca.buscar_por_autor(autor))

@app.route("/libros/titulo/<titulo>")
def buscar_titulo(titulo):
    return jsonify(biblioteca.buscar_por_titulo(titulo))

if __name__ == "__main__":
    app.run(debug=True)
    
