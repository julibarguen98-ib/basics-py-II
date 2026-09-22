"""
--------------------------- FUNCIONES ---------------------------
En este taller aprenderás a crear funciones en Python, desde las básicas hasta las que retornan valores, manejo de errores y excepciones, y su uso en clases.
"""


"""
--- Ejercicio 1: Función para Agregar Libros ---
Crea una función llamada `agregar_libro` que acepte dos parámetros, `titulo` y `autor`,
y que retorne un diccionario con el título y el autor del libro.
"""

# Escribe tu código aquí
def agregar_libro(titulo, autor):
  return {"titulo":titulo, "autor":autor}
# Prueba la función con algunos valores
libro = agregar_libro("Cerdos en la sala", "Frank Hammon")
print(libro)

"""
--- Ejercicio 2: Función para Listar Libros ---
Crea una función llamada `listar_libros` que acepte una lista de diccionarios `libros` y 
que retorne una lista con los títulos de los libros.
"""

# Escribe tu código aquí
def listar_libros(libros):
  titulos = []
  for libro in libros:
    titulos.append(libro["titulo"])
  return titulos
  # Prueba la función con algunos valores
libros = [
  {"titulo": "Hansell & Gretell", "autor": "Hermanos Grimm"},
  {"titulo": "El gigante egoista", "autor": "Oscar Wilde"},
  {"titulo": "Hermes y el hacha", "autor": "Esopo"}
  ]
  
lista = listar_libros(libros)
print(lista)

"""
--- Ejercicio 3: Función para Buscar Libros ---
Crea una función llamada `buscar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne el diccionario del libro que coincida con el título, o `None` si no se encuentra.
"""

# Escribe tu código aquí
def buscar_libro (libros, titulo):
  for libro in libros:
    if libro["titulo"] == titulo:
      return libro
  return None
# Prueba la función con algunos valores
libros = [
  {"titulo": "Hansell & Gretell", "autor": "Hermanos Grimm"},
  {"titulo": "El gigante egoista", "autor": "Oscar Wilde"},
  {"titulo": "Hermes y el hacha", "autor": "Esopo"}
  ]

print(buscar_libro(libros,"El gigante egoista"))
print(buscar_libro(libros, "La cenicienta"))
"""
--- Ejercicio 4: Manejo de Errores ---
Crea una función llamada `quitar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que intente quitar el libro con el título especificado. Si no se encuentra el libro, maneja el error adecuadamente.
"""

# Escribe tu código aquí
def quitar_libro(libros, titulo):
  try:
    for libro in libros:
      if libro["titulo"] == titulo:
        libros.remove(libro)
        return libros

    raise ValueError("Libro no encontrado")
  except ValueError as error:
    print(error)
    return libros
# Prueba la función con algunos valores
libros = [
  {"titulo": "Hansell & Gretell", "autor": "Hermanos Grimm"},
  {"titulo": "El gigante egoista", "autor": "Oscar Wilde"},
  {"titulo": "Hermes y el hacha", "autor": "Esopo"}
  ]

print(quitar_libro(libros,"El gigante egoista"))
print(quitar_libro(libros, "La cenicienta"))

"""
--- Ejercicio 5: Función que Retorna un Diccionario ---
Crea una función llamada `crear_inventario` que acepte una lista de diccionarios `libros` y 
que retorne un diccionario con la cantidad de libros por autor.
"""

# Escribe tu código aquí
def crear_inventario(libros):
  inventario = {}
  for libro in libros:
    autor = libro["autor"]
    if autor in inventario:
      inventario[autor] += 1
    else :
      inventario[autor] = 1
  return inventario
# Prueba la función con algunos valores
libros = [
  {"titulo": "Hansell & Gretell", "autor": "Hermanos Grimm"},
  {"titulo": "Blancanieves", "autor": "Hermanos Grimm"},
  {"titulo": "Hermes y el hacha", "autor": "Esopo"}
  ]

print(crear_inventario(libros))

"""
--- Ejercicio 6: Función que Retorna una Lista ---
Crea una función llamada `libros_por_autor` que acepte una lista de diccionarios `libros` y un `autor` y 
que retorne una lista con los títulos de los libros escritos por el autor especificado.
"""

# Escribe tu código aquí
def libros_por_autor(libros, autor):
  titulos = []
  for libro in libros:
    if libro["autor"] == autor:
      titulos.append(libro["titulo"])
  return titulos
# Prueba la función con algunos valores
libros = [
  {"titulo": "Hansell & Gretell", "autor": "Hermanos Grimm"},
  {"titulo": "Blancanieves", "autor": "Hermanos Grimm"},
  {"titulo": "Hermes y el hacha", "autor": "Esopo"}
  ]

print(libros_por_autor(libros, "Hermanos Grimm"))

"""
--- Ejercicio 7: Función que Retorna un Booleano ---
Crea una función llamada `existe_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne `True` si el libro existe en la lista, y `False` en caso contrario.
"""

# Escribe tu código aquí
def existe_libro(libros, titulo):
  for libro in libros:
    if libro["titulo"] == titulo:
      return True
  return False
# Prueba la función con algunos valores
libros = [
  {"titulo": "Hansell & Gretell", "autor": "Hermanos Grimm"},
  {"titulo": "Hermes y el hacha", "autor": "Esopo"}
  ]

print(existe_libro(libros, "Hansell & Gretell"))
print(existe_libro(libros, "Aladino"))
