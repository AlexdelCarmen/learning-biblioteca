import json
import os

PATH_BIBLIOTECA = "biblioteca.json"

try:
    with open (PATH_BIBLIOTECA) as biblioteca_json:
        lista_de_libros = json.load(biblioteca_json)
except FileNotFoundError: 
    lista_de_libros = {}
    print("Archivo no encontrado")


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

def listar_libros(biblioteca):
    return(biblioteca)

def obtener_resultados(resultados):
    if len(resultados) == 0:
        print("No se encontraron resultados")
    else: 
        print(resultados)

def menu_biblioteca(): 
    looping = True
    while looping: 
        print(("=== Bienvenido a la Bibliteca ===\n"
                "1. Ver todos los libros\n"
                "2. Buscar por autor\n"        
                "3. Buscar por titulo\n"
                "4. Agregar libro\n"
                "5. Salir"))
        seleccion = input("Elige una opcion: ")
        
        if seleccion == 1: 
            print(listar_libros(lista_de_libros))
        
        elif seleccion == 2:
            autor = input("Ingresa el nombre del autor: ")
            resultados = buscar_por_autor(lista_de_libros, autor)
            obtener_resultados(resultados)
        
        elif seleccion == 3: 
            titulo = input("Ingresa el titulo: ")
            resultados = buscar_por_titulo(lista_de_libros, titulo)
            obtener_resultados(resultados)
        
        elif seleccion == 4: 
            autor = input("Ingresa el autor: ")
            titulo = input("Ingresa el titulo: ")
            año = int(input("Ingresa el año: "))
            genero = input("Ingresa el genero: ")
            agregar_libro(lista_de_libros, autor, titulo, año, genero)
            print("Agregado con exito!")

        
        elif seleccion == 5: 
            looping = False
        
        else: 
            print("Opcion no valida. Intenta de nuevo")

menu_biblioteca()