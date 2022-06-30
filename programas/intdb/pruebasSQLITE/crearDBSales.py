#SQLite es la base de datos con la cual es más fácil conectarse desde Python.

#No se tiene que instalar ni configurar ningún servidor, solo importar la biblioteca sqlite3

#SQLITE graba y escribe todos los datos en un solo archivo.

import sqlite3                           # Biblioteca con sqlite
from sqlite3 import Error                # Accede a Error generado en funciones de sqlite

nombreDB="salesdata.db"

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

#OrderID,Quantity,UnitPrice(USD),
# Status,OrderDate,Product_Category,
# Sales_Manager,Shipping_Cost(USD),
# Delivery_Time(Days),Shipping_Address,Product_Code,OrderCode

crear_tabla_de_ventas = """
CREATE TABLE IF NOT EXISTS salesData (
  order_id TEXT(24) NOT NULL,
  quantity DECIMAL NOT NULL,
  unit_price DECIMAL NOT NULL,
  status TEXT NOT NULL,
  order_date DATE NOT NULL,
  product_category TEXT NOT NULL,
  sales_manager TEXT NOT NULL,
  shipping_cost DECIMAL NOT NULL,
  delivery_time INTEGER,
  shipping_address TEXT NOT NULL,
  product_code TEXT NOT NULL,
  order_code TEXT NOT NULL)
  ;

"""


comandos = []

comandos.append(crear_tabla_de_ventas)

#### Se conecta a la base de datos. Si no existe, la crea vacía

conexion=crear_conexion(nombreDB)

###  Crea las estructuras vácías de cada una de las tablas

for cmd in comandos:
    ejecutar_comando_sql(conexion, cmd, msg=" Creando bd ") 

