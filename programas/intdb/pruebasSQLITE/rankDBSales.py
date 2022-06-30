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
 SELECT product_category, shipping_address, shipping_cost,
        ROW_NUMBER() OVER
           (PARTITION BY product_category, shipping_address
            ORDER BY shipping_cost DESC) 
        AS Number,
        RANK() OVER
           (PARTITION BY product_category, shipping_address
            ORDER BY shipping_cost DESC)
        AS Rank,
        DENSE_RANK() OVER
           (PARTITION BY product_category, shipping_address
            ORDER BY shipping_cost DESC)
        AS DenseRank
        FROM salesData
        WHERE product_category IS NOT NULL 
              AND shipping_address IN ('Germany','India')
              AND status in ('Delivered')         
        '''
        
comando2='''
     WITH SM AS MATERIALIZED
     (SELECT DISTINCT sales_manager FROM salesData
          WHERE shipping_address = 'Germany' and unit_price > 150.0
    ), PC AS MATERIALIZED
    
    (SELECT DISTINCT product_category FROM salesData
            WHERE product_category = 'Healthcare' AND unit_price > 150.0
    
    )
    
    SELECT sales_manager,
        product_category,
        unit_price
        FROM salesData
        WHERE product_category IN (
            SELECT product_category FROM PC)
        AND sales_manager IN (
                SELECT sales_manager FROM SM
            )
        AND unit_price > 150.0
    ORDER BY unit_price DESC
    '''

show_results(conexion, comando ,msg="Lista de VENTAS 1")
#show_results(conexion, comando2 ,msg="Lista de VENTAS 2")
#show_results(conexion, comando3 ,msg="Lista de VENTAS 3")      
        
        
