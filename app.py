
from logica import Biblioteca

biblioteca = Biblioteca()
            
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
            biblioteca.imprimir_lista()
        
        elif seleccion == 2:
            autor = input("Ingresa el nombre del autor: ")
            resultados = biblioteca.buscar_por_autor(autor)
            obtener_resultados(resultados)
        
        elif seleccion == 3: 
            titulo = input("Ingresa el titulo: ")
            resultados = biblioteca.buscar_por_titulo(titulo)
            obtener_resultados(resultados)
        
        elif seleccion == 4: 
            titulo = input("Ingresa el titulo: ")
            autor = input("Ingresa el autor: ")
            año = int(input("Ingresa el año: "))
            genero = input("Ingresa el genero: ")
            biblioteca.agregar_libro(titulo, autor, año, genero)
            print("Agregado con exito!")

        
        elif seleccion == 5: 
            looping = False
        
        else: 
            print("Opcion no valida. Intenta de nuevo")

menu_biblioteca()