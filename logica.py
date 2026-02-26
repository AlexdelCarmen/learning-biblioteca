import os
import json
import pprint
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

class Base(DeclarativeBase):
    pass

class Libro(Base): 
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor = Column(String)
    año = Column(Integer)
    genero = Column(String)
    
engine = create_engine("sqlite:///biblioteca.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

'''BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_BIBLIOTECA = os.path.join(BASE_DIR, "biblioteca.json")'''

class Biblioteca: 
    def __init__(self):
        
        '''try:
            with open(PATH_BIBLIOTECA) as biblioteca_json:
                self.libros = json.load(biblioteca_json)
        except FileNotFoundError:
            self.libros = []
            print("Archivo no encontrado")'''
    
    def imprimir_lista(self):
        with Session() as session: 
            print(session.query(Libro).all())
        
    def agregar_libro(self, titulo, autor, año, genero): 
        with Session() as session: 
            nuevo_libro = Libro(titulo=titulo, autor=autor, año=año, genero=genero)
            session.add(nuevo_libro)
            session.commit
        
    '''def _buscar_biblioteca(self, parametro, valor):
        resultado = self.libros.session.query(Libro).filter_by(parametro=valor).first()
        return resultado'''

    def buscar_por_autor(self, autor): 
        return self._buscar_biblioteca("autor", autor)

    def buscar_por_titulo(self, titulo):
        return self._buscar_biblioteca("titulo", titulo)