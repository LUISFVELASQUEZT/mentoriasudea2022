#SQLite es la base de datos con la cual es más fácil conectarse desde Python.

#No se tiene que instalar ni configurar ningún servidor, solo importar la biblioteca sqlite3

#SQLITE graba y escribe todos los datos en un solo archivo.

# Ejemplos basados en tutoriales en https://realpython.com/

import sqlite3
from sqlite3 import Error

nombreDB="personas.db"

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

show_results(conexion, comando="SELECT * from padres",msg="Lista de padres")
show_results(conexion, comando="SELECT * FROM hijos",msg="Lista de hijos")
show_results(conexion, msg="Join hijos padres ", comando=
"SELECT cedula, padres.nombres, padres.apellidos, direccion, documento_id, hijos.nombres, hijos.apellidos FROM hijos INNER JOIN padres ON padres.cedula = hijos.cedula_padre;")  
show_results(conexion, msg="Join padres hijos ", comando=
"SELECT cedula, p.nombres, p.apellidos, direccion, documento_id, hijos.nombres, hijos.apellidos FROM padres p INNER JOIN hijos ON hijos.cedula_padre = p.cedula;")     
       
        
        
