#SQLite es la base de datos con la cual es más fácil conectarse desde Python.

#No se tiene que instalar ni configurar ningún servidor, solo importar la biblioteca sqlite3

#SQLITE graba y escribe todos los datos en un solo archivo.

import sqlite3                           # Biblioteca con sqlite
from sqlite3 import Error                # Accede a Error generado en funciones de sqlite

nombreDB="employees.db"

#### Se conecta a la base de datos. Si la bd no existe, la crea vacía

def crear_conexion(nombreDB):
    conexion = None
    try:
        conexion = sqlite3.connect(nombreDB)
        print(f"Conexión exitosa a {nombreDB} SQLITE")
    except Error as e:
        print(f"Ocurrió el error {e} al intentar conectarse a {nombreDB}")
    return conexion

def ejecutar_comando_sql(conexion, comando, msg):
    cursor = conexion.cursor()
    try:
        print(f'{"*" * len(msg)} Inicio de {msg} {"*" * len(msg)}')
        cursor.execute(comando)
        conexion.commit()
    except Error as e:
        print(f"Ocurrió el error '{e}' al ejecutar el comando {comando}")

### Instrucciones tipo DDL (Data Definition Language)   
#   Usa syntaxis propia de SQLITE3     

crear_tabla_de_ventas = '''
CREATE TABLE IF NOT EXISTS employees (
  EmployeeName TEXT NOT NULL,
  EmployeeID   CHAR(6) NOT NULL,
  ManagerID    CHAR(6),
  TotalOrders  DECIMAL NOT NULL
  )
'''

comandos = []

comandos.append(crear_tabla_de_ventas)

#### Se conecta a la base de datos. Si no existe, la crea vacía

conexion=crear_conexion(nombreDB)

###  Crea las estructuras vácías de cada una de las tablas

for cmd in comandos:
    ejecutar_comando_sql(conexion, cmd, msg=" Creando bd ") 

