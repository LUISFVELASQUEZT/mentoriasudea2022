#SQLite es la base de datos con la cual es más fácil conectarse desde Python.

#No se tiene que instalar ni configurar ningún servidor, solo importar la biblioteca sqlite3

#SQLITE graba y escribe todos los datos en un solo archivo.

import sqlite3                           # Biblioteca con sqlite
from sqlite3 import Error                # Accede a Error generado en funciones de sqlite

nombreDB="personas.db"

#### Se conecta a la base de datos. Si la bd no existe, la crea vacía

def crear_conexion(nombreDB):
    conexion = None
    try:
        conexion = sqlite3.connect(nombreDB)
        print(f"Conexión exitosa a {nombreDB} SQLITE")
    except Error as e:
        print(f"Ocurrió el error {e} al intentar conectarse a {nombreDB}")
    return conexion

def ejecutar_comando_sql(conexion, comando):
    cursor = conexion.cursor()
    try:
        cursor.execute(comando)
        conexion.commit()
    except Error as e:
        print(f"Ocurrió el error '{e}' al ejecutar el comando {comando}")

### Instrucciones tipo DDL (Data Definition Language)   
#   Usa syntaxis propia de SQLITE3     

cargar_tabla_de_padres = """
INSERT INTO padres (cedula, nombres, apellidos, direccion)
VALUES
  ("12.123.456.8","Pedro Luis", "Gonzalez Serna","Carrera 80 51AA72,Medellín"),
  ("77.123.456.8","Luis Armando", "Ramírez Gómez","Carrera 90 41A72,Medellín")
;
"""

### Instrucciones tipo DDL (Data Definition Language)   
#   Usa syntaxis propia de SQLITE3  
cargar_tabla_de_hijos = """
INSERT INTO hijos (documento_id, nombres, apellidos, cedula_padre)
VALUES
  ("123","Luis Jr.", "Gonzalez","12.123.456.8"),
  ("124","Luisa Jr.", "Gonzalez","12.123.456.8"),
  ("246","Luis Armando Jr.", "Ramírez","77.123.456.8"),
  ("1246","Luisa Fernanda", "Ramírez","77.123.456.8")
;
"""
#### Se conecta a la base de datos. Si no existe, la crea vacía

conexion=crear_conexion(nombreDB)

###  Crea las estructuras vácías de cada una de las tablas

ejecutar_comando_sql(conexion, cargar_tabla_de_padres)

ejecutar_comando_sql(conexion, cargar_tabla_de_hijos) 
