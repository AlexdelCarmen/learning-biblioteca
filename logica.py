import os
import json
import pprint
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_BIBLIOTECA = os.path.join(BASE_DIR, "biblioteca.json")

class Biblioteca: 
    def __init__(self):
        
        try:
            with open(PATH_BIBLIOTECA) as biblioteca_json:
                self.libros = json.load(biblioteca_json)
        except FileNotFoundError:
            self.libros = []
            print("Archivo no encontrado")
    
    def imprimir_lista(self):
        pprint.pprint(self.libros)
        
    def agregar_libro(self, titulo, autor, año, genero): 
        nuevo_libro = {"titulo" : titulo, "autor": autor, "año": año, "genero": genero}
        self.libros.append(nuevo_libro)
        with open (PATH_BIBLIOTECA, "w") as f: 
            json.dump(self.libros, f, indent=4)   
        
    def _buscar_biblioteca(self, parametro, valor):
        resultado = [libro for libro in self.libros if libro[parametro] == valor]
        return resultado

    def buscar_por_autor(self, autor): 
        return self._buscar_biblioteca("autor", autor)

    def buscar_por_titulo(self, titulo):
        return self._buscar_biblioteca("titulo", titulo)