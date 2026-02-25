import os
import json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_BIBLIOTECA = os.path.join(BASE_DIR, "biblioteca.json")

def agregar_libro(biblioteca, titulo, autor, año, genero): 
    nuevo_libro = {"titulo" : titulo, "autor": autor, "año": año, "genero": genero}
    biblioteca.append(nuevo_libro)
    with open (PATH_BIBLIOTECA, "w") as f: 
        json.dump(biblioteca, f, indent=4)

def buscar_biblioteca(biblioteca, parametro, valor):
    resultado = [libro for libro in biblioteca if libro[parametro] == valor]
    return(resultado)

def buscar_por_autor(biblioteca, autor): 
    return(buscar_biblioteca(biblioteca, "autor", autor))

def buscar_por_titulo(biblioteca, titulo):
    return(buscar_biblioteca(biblioteca, "titulo", titulo))