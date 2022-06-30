#SQLite es la base de datos con la cual es más fácil conectarse desde Python.

#No se tiene que instalar ni configurar ningún servidor, solo importar la biblioteca sqlite3

#SQLITE graba y escribe todos los datos en un solo archivo.

import sqlite3                           # Biblioteca con sqlite
from sqlite3 import Error                # Accede a Error generado en funciones de sqlite
import csv

csv_fn = "../mentoriasudea2022/data/employees.csv"
nombreDB="employees.db"

#### Se conecta a la base de datos. Si la bd no existe, la crea vacía
fila= []

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
        
def f_cargar_empleados():
    empName = fila['EmployeeName']
    empID = fila['EmployeeID']
    supID = fila['ManagerID']
    totalOrders = float(fila['TotalOrders'])
        
    comando="""insert into employees (
               EmployeeName,
               EmployeeID,
               ManagerID,
               TotalOrders
               )
               values (?,?,?,?)
               """
    
    ejecutar_comando_sql(conexion, comando, (
        empName, empID, supID, totalOrders
    ))

#### Se conecta a la base de datos. Si no existe, la crea vacía

conexion=crear_conexion(nombreDB)

with open (csv_fn,'r') as fn:  #  Se define contexto para el proceso siguiente
    lector = csv.DictReader(fn)          #  Objeto lector con el método reader de csv
    
    for fila in lector:  
        f_cargar_empleados()       
    