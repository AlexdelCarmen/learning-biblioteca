import os
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
    def to_dict(self): 
        return {"id": self.id, "titulo": self.titulo, "autor": self.autor, "año": self.año, "genero": self.genero}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "biblioteca.db")

engine = create_engine(f"sqlite:///{DB_PATH}")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

class Biblioteca: 
    
    def obtener_libros(self):
        with Session() as session: 
            return [libro.to_dict() for libro in session.query(Libro).all()]
        
    def agregar_libro(self, titulo, autor, año, genero): 
        with Session() as session: 
            nuevo_libro = Libro(titulo=titulo, autor=autor, año=año, genero=genero)
            session.add(nuevo_libro)
            session.commit()
    
    def buscar_por_autor(self, valor): 
        with Session() as session: 
            return [libro.to_dict() for libro in session.query(Libro).filter_by(autor=valor).all()]

    def buscar_por_titulo(self, valor):
        with Session() as session: 
            return [libro.to_dict() for libro in session.query(Libro).filter_by(titulo=valor).all()]
