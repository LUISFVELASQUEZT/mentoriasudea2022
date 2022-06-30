#SQLite es la base de datos con la cual es más fácil conectarse desde Python.

#No se tiene que instalar ni configurar ningún servidor, solo importar la biblioteca sqlite3

#SQLITE graba y escribe todos los datos en un solo archivo.

# Ejemplos basados en tutoriales en https://realpython.com/

import sqlite3
from sqlite3 import Error

nombreDB="salesdata.db"

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
        
def show_results(conexion, comando,msg):
    resultado = ejecutar_consulta (conexion, comando)
    print(f'{"*" * len(msg)} Inicio de {msg} {"*" * len(msg)}')
    for dato in resultado:
         print(dato)
    print(f'{"=" * len(msg)} Final de {msg} {"=" * len(msg)}')
      
        
conexion=crear_conexion(nombreDB)

comando='''
 SELECT strftime ('%m',order_date)
        AS Month,
        SUM(quantity) AS TotalQty
        FROM salesData
        GROUP BY strftime('%m', order_date)                      
        '''
        
comando='''
 SELECT strftime ('%S',order_date)
        AS Dow,
        SUM(quantity) AS TotalQty
        FROM salesData
        GROUP BY strftime('%S', order_date)                      
        '''
show_results(conexion, comando ,msg="Lista de VENTAS 1")
#show_results(conexion, comando2 ,msg="Lista de VENTAS 2")
#show_results(conexion, comando3 ,msg="Lista de VENTAS 3")      
        
        
