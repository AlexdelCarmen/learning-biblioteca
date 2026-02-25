import json
import pprint
from logica import agregar_libro, buscar_por_autor, buscar_por_titulo, PATH_BIBLIOTECA


try:
    with open (PATH_BIBLIOTECA) as biblioteca_json:
        lista_de_libros = json.load(biblioteca_json)
except FileNotFoundError: 
    lista_de_libros = {}
    print("Archivo no encontrado")

            
# Despliega resultados para busquedas o imprime un error si no hay matches
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
        try: 
            seleccion = int(input("Elige una opcion: "))
        except ValueError:
            print("Ingresa un numero valido")
            continue
        
        if seleccion == 1: 
            pprint.pprint(lista_de_libros)
        
        elif seleccion == 2:
            autor = input("Ingresa el nombre del autor: ")
            resultados = buscar_por_autor(lista_de_libros, autor)
            obtener_resultados(resultados)
        
        elif seleccion == 3: 
            titulo = input("Ingresa el titulo: ")
            resultados = buscar_por_titulo(lista_de_libros, titulo)
            obtener_resultados(resultados)
        
        elif seleccion == 4: 
            titulo = input("Ingresa el titulo: ")
            autor = input("Ingresa el autor: ")
            año = int(input("Ingresa el año: "))
            genero = input("Ingresa el genero: ")
            agregar_libro(lista_de_libros, titulo, autor, año, genero)
            print("Agregado con exito!")

        
        elif seleccion == 5: 
            looping = False
        
        else: 
            print("Opcion no valida. Intenta de nuevo")

menu_biblioteca()