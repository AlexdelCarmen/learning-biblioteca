books = {
    "titulo": "El Hobbit",
    "autor": "JRR Tolkien",
    "año": 1958, 
    "genero": "Fantasia"    
}

print(books)

lista_de_libros = [
    {
    "titulo": "El Hobbit",
    "autor": "JRR Tolkien",
    "año": 1958, 
    "genero": "Fantasia"    
    },
    {
    "titulo": "La Comunidad del Anillo",
    "autor": "JRR Tolkien",
    "año": 1978, 
    "genero": "Fantasia"    
    },
    {
    "titulo": "Libros de Sangre 1",
    "autor": "Clive Barker",
    "año": 2001, 
    "genero": "Terror"    
    }
]

def agregar_libro(biblioteca, titulo, autor, año, genero): 
    nuevo_libro = {"titulo" : titulo}, {"autor": autor}, {"año": año}, {"genero": genero}
    biblioteca.append(nuevo_libro)
    print(biblioteca)

'''for libro in lista_de_libros: 
    print(f"{libro["autor"]} : {libro["titulo"]}")
'''

def buscar_biblioteca(biblioteca, parametro, valor):
    resultado = [libro for libro in biblioteca if libro[parametro] == valor]
    return resultado

def buscar_por_autor(biblioteca, autor): 
    return(buscar_biblioteca(biblioteca, "autor", autor))

def buscar_por_titulo(biblioteca, titulo):
    return(buscar_biblioteca(biblioteca, "titulo", titulo))

''' resultados = buscar_por_autor(lista_de_libros, "nadie")
if len(resultados) == 0: 
    print("no se encontraron resultados")
else:
    print(resultados)
'''

agregar_libro(lista_de_libros, "El Pescador", "John Langan", 2021, "Terror")
