#SQLite es la base de datos con la cual es más fácil conectarse desde Python.

#No se tiene que instalar ni configurar ningún servidor, solo importar la biblioteca sqlite3

#SQLITE graba y escribe todos los datos en un solo archivo.

import sqlite3                           # Biblioteca con sqlite
from sqlite3 import Error                # Accede a Error generado en funciones de sqlite

nombreDB="testfac.db"

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
        cursor.execute(comando[1])
        conexion.commit()
    except Error as e:
        print(f"Ocurrió el error '{e}' al ejecutar el comando {comando}")

### Instrucciones tipo DDL (Data Definition Language)   
#   Usa syntaxis propia de SQLITE3     

def f_comandos():
    
    crear_tabla_de_clientes = ["Crear tabla de clientes", """
        CREATE TABLE IF NOT EXISTS clientes (
        nit CHAR(12) NOT NULL PRIMARY KEY,
        nombres TEXT NOT NULL);
        """]

### Instrucciones tipo DDL (Data Definition Language)   
#   Usa syntaxis propia de SQLITE3  

    crear_tabla_de_productos = ["Creando tabla de productos ", """
        CREATE TABLE IF NOT EXISTS productos(
        id_producto CHAR(12) PRIMARY KEY,
        descripcion TEXT NOT NULL);
        """]

    crear_tabla_de_facturas = ["Creando tabla de facturas", """
        CREATE TABLE IF NOT EXISTS facturas(
        id_documento CHAR(12) PRIMARY KEY,
        descripcion TEXT NOT NULL,
        fecha timedate,
        valor DECIMAL, 
        nit,
        FOREIGN KEY (nit) REFERENCES clientes (nit));
        """]

    crear_tabla_de_ventas = ["Crear tabla de ventas", """
        CREATE TABLE IF NOT EXISTS ventas(
        id_documento CHAR(12) NOT NULL,
        id_producto CHAR(12) NOT NULL,
        fecha timedate,
        cantidad DECIMAL,
        valor DECIMAL,
        costo DECIMAL,
        PRIMARY KEY (id_documento, id_producto)
        FOREIGN KEY (id_producto) REFERENCES productos (id_producto)
        FOREIGN KEY (id_documento) REFERENCES facturas (id_documento)
        );
        """]
    
    comandos = []
    comandos.append(crear_tabla_de_clientes)
    comandos.append(crear_tabla_de_productos)
    comandos.append(crear_tabla_de_facturas)
    comandos.append(crear_tabla_de_ventas)
    return comandos
#### Se conecta a la base de datos. Si no existe, la crea vacía

conexion=crear_conexion(nombreDB)

###  Crea las estructuras vácías de cada una de las tablas

comandos=f_comandos()

for cmd in comandos:
    print(f'{cmd[0]} {cmd[1]}')
    ejecutar_comando_sql(conexion, cmd) 

