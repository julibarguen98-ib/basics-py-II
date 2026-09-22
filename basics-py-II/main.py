# Añade una colección de libros
from libreria import (
    agregar_libro,
    libros_por_autor,
    existe_libro
)
libros = [
  agregar_libro("Cerdos en la sala", "Frank Hammon"),
  agregar_libro("Hansell & Gretell", "Hermanos Grimm"),
  agregar_libro("Hermes y el hacha", "Esopo"),
  agregar_libro("Blancanieves", "Hermanos Grimm"),
  agregar_libro("El gigante egoista", "Oscar Wilde")
]
# Muestra la colección de libros creada
print("Colección de libros:")
print(libros)
# Busca un libro por el autor
print("\nLibros de Hermanos Grimm:")
print(libros_por_autor(libros, "Hermanos Grimm"))
# Verifica si un libro está disponible
print("\n¿Existe Blancanieves?")
print(existe_libro(libros, "Blancanieves"))