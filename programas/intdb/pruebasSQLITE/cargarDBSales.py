#SQLite es la base de datos con la cual es más fácil conectarse desde Python.

#No se tiene que instalar ni configurar ningún servidor, solo importar la biblioteca sqlite3

#SQLITE graba y escribe todos los datos en un solo archivo.

import sqlite3                           # Biblioteca con sqlite
from sqlite3 import Error                # Accede a Error generado en funciones de sqlite
import csv

csv_fn = "../mentoriasudea2022/data/DummySalesData.csv"
nombreDB="salesdata.db"

#### Se conecta a la base de datos. Si la bd no existe, la crea vacía
fila= []
cntSinDeliveryTime=0
cntRegistros = 0

def crear_conexion(nombreDB):
    conexion = None
    try:
        conexion = sqlite3.connect(nombreDB)
        print(f"Conexión exitosa a {nombreDB} SQLITE")
    except Error as e:
        print(f"Ocurrió el error {e} al intentar conectarse a {nombreDB}")
    return conexion

def ejecutar_comando_sql(conexion, comando, par):
    cursor = conexion.cursor()
    try:
        cursor.execute(comando,par)
        conexion.commit()
    except Error as e:
        print(f"Ocurrió el error '{e}' al ejecutar el comando {comando}")
        
def f_cargar_productos():
    cntRegistros=+1
    orderID = fila['OrderID']
    quantity = float(fila['Quantity'])
    unitPrice = float(fila['UnitPrice(USD)'])
    status = fila['Status']
    orderDate = fila['OrderDate']
    productCategory = fila['Product_Category']
    salesManager = fila['Sales_Manager']
    shippingCost = float(fila['Shipping_Cost(USD)'])
    deliveryTime=0
    try:
        deliveryTime=int(fila['Delivery_Time(Days)'])
    except ValueError:
        deliveryTime = 0
        cntSinDeliveryTime=+1
    shippingAddress=fila['Shipping_Address']
    productCode=fila['Product_Code']
    orderCode=fila['OrderCode']  
      
    comando="""insert into salesData (
               order_id,
               quantity,
               unit_price,
               status,
               order_date,
               product_category,
               sales_manager,
               shipping_cost,
               delivery_time,
               shipping_address,
               product_code,
               order_code
               )
               values (?,?,?,?,?,?,?,?,?,?,?,?)
               """
    
    ejecutar_comando_sql(conexion, comando, (
        orderID, quantity, unitPrice,
        status, orderDate, productCategory, 
        salesManager, shippingCost, deliveryTime, 
        shippingAddress, productCode, orderCode
    ))

#### Se conecta a la base de datos. Si no existe, la crea vacía

conexion=crear_conexion(nombreDB)

with open (csv_fn,'r') as fn:  #  Se define contexto para el proceso siguiente
    lector = csv.DictReader(fn)          #  Objeto lector con el método reader de csv
    
    for fila in lector:  
        f_cargar_productos()       
    print(f'Registros {cntRegistros} sin delivery {cntSinDeliveryTime}')