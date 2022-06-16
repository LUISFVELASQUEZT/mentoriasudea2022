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

crear_tabla_de_padres = """
CREATE TABLE IF NOT EXISTS padres (
  cedula CHAR(12) NOT NULL PRIMARY KEY,
  nombres TEXT NOT NULL,
  apellidos TEXT NOT NULL,
  direccion TEXT  
);
"""

### Instrucciones tipo DDL (Data Definition Language)   
#   Usa syntaxis propia de SQLITE3  

crear_tabla_de_hijos = """
CREATE TABLE IF NOT EXISTS hijos(
  documento_id CHAR(12) PRIMARY KEY,
  nombres TEXT NOT NULL,
  apellidos TEXT NOT NULL,  
  cedula_padre CHAR(12) NOT NULL,
  FOREIGN KEY (cedula_padre) REFERENCES padres (cedula)  
);
"""

#### Se conecta a la base de datos. Si no existe, la crea vacía

conexion=crear_conexion(nombreDB)

###  Crea las estructuras vácías de cada una de las tablas

ejecutar_comando_sql(conexion, crear_tabla_de_padres)

ejecutar_comando_sql(conexion, crear_tabla_de_hijos) 




