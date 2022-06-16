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
        print(f"Conexión exitosa a {nombreDB} SQLITE")
    except Error as e:
        print(f"Ocurrió el error {e} al intentar conectarse a {nombreDB}")

    return conexion

def consultar_publicaciones(conexion, id):
    cursor = conexion.cursor()
    resultado = None
    
    try:
        cursor.execute('''select * from publicaciones where id = ?''',(id,))
        datosConsulta = cursor.fetchall()
        
    except Error as e:
        print(f" Ocurrio el error '{e}' al ejecutar el comando '{comando}'")
        
    for dato in datosConsulta:
        print(dato)   

def ejecutar_comando_sql(conexion, comando):
    cursor = conexion.cursor()
    try:
        cursor.execute(comando)
        conexion.commit()
        print(f"Comando ejecutado exitosamente")
    except Error as e:
        print(f"Ocurrió el error '{e}' al ejecutar el comando {comando}")

conexion=crear_conexion(nombreDB)

consultar_publicaciones(conexion, 5)

comando = """
UPDATE
  publicaciones
SET
  descripcion = "22222222222222222222222222"
WHERE
  id = 5
"""

ejecutar_comando_sql(conexion, comando)

consultar_publicaciones(conexion, 5)

comando = """
DELETE FROM
  publicaciones
WHERE
  id = 5
"""

ejecutar_comando_sql(conexion, comando)
consultar_publicaciones(conexion, 5)



