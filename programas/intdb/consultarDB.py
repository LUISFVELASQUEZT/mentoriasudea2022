#SQLite es la base de datos con la cual es más fácil conectarse desde Python.

#No se tiene que instalar ni configurar ningún servidor, solo importar la biblioteca sqlite3

#SQLITE graba y escribe todos los datos en un solo archivo.

# Ejemplos basados en tutoriales en https://realpython.com/

import sqlite3
from sqlite3 import Error

nombreDB="miBlog.db"

def crear_conexion(nombreDB):
    conexion = None
    try:
        conexion = sqlite3.connect(nombreDB)
        print(f"Conexión exitosa a a {nombreDB} SQLITE")
    except Error as e:
        print(f"Ocurrió el error {e} al intentar conectarse a {nombreDB}")

    return conexion

def ejecutar_consulta(conexion, comando):
    cursor = conexion.cursor()
    resultado = None
    try:
        cursor.execute(comando)
        resultado = cursor.fetchall()
        return resultado
    except Error as e:
        print(f" Ocurrio el error '{e}' al ejecutar el comando '{comando}'")        
        
conexion=crear_conexion(nombreDB)

comando = "SELECT nombres, apellidos, edad, genero from usuarios order by nombres,apellidos"
datosUsuarios = ejecutar_consulta (conexion, comando)

for dato in datosUsuarios:
    print(dato)

comando = "SELECT * FROM publicaciones order by id_usuario, titulo"
datosPublicaciones = ejecutar_consulta (conexion, comando)

for dato in datosPublicaciones:
    print(dato)

comando = """
SELECT
  usuarios.id,
  usuarios.nombres,
  publicaciones.descripcion
FROM
  publicaciones
  INNER JOIN usuarios ON usuarios.id = publicaciones.id_usuario
  order by usuarios.nombres
"""

datosUPublicaciones = ejecutar_consulta(conexion, comando)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
for dato in datosUPublicaciones:
    print(dato)
    
comando = """
SELECT
  publicaciones.descripcion as Publicacion,
  comentario as Commentario,
  comentarios.fecha,
  nombres
FROM
  publicaciones
  INNER JOIN comentarios ON publicaciones.id = comentarios.id_publicacion
  INNER JOIN usuarios ON usuarios.id = comentarios.id_usuario
"""
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

cursor = conexion.cursor()
cursor.execute(comando)
cursor.fetchall()

column_names = [description[0] for description in cursor.description]
print(column_names)

datosUComentarios = ejecutar_consulta(conexion, comando)

for dato in datosUComentarios:
    print(dato)    
    
print(">>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<")    
comando = """
SELECT
    COUNT(me_gusta.id) as MeGusta,
    descripcion as Publicacion
FROM
  me_gusta,
  publicaciones
WHERE
  publicaciones.id = me_gusta.id_publicacion
GROUP BY
  me_gusta.id_publicacion
"""

datosPubMegusta = ejecutar_consulta(conexion, comando)

for dato in datosPubMegusta:
    print(dato)

