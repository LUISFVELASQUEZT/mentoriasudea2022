#SQLite es la base de datos con la cual es más fácil conectarse desde Python.

#No se tiene que instalar ni configurar ningún servidor, solo importar la biblioteca sqlite3

#SQLITE graba y escribe todos los datos en un solo archivo.

import sqlite3                           # Biblioteca con sqlite
from sqlite3 import Error                # Accede a Error generado en funciones de sqlite
import csv

csv_fn = "../mentoriasudea2022/data/prueba3NF.csv"
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

def ejecutar_comando_sql(conexion, comando, par):
    cursor = conexion.cursor()
    try:
        cursor.execute(comando,par)
        conexion.commit()
    except Error as e:
        print(f"Ocurrió el error '{e}' al ejecutar el comando {comando}")
        
def ejecutar_consulta_un_registro (conexion, comando, par):
    cursor = conexion.cursor()
    resultado = None
    try:
        cursor.execute(comando,par)
        resultado = cursor.fetchone()
        return resultado
    except Error as e:
        print(f" Ocurrio el error '{e}' al ejecutar el comando '{comando}'")
        
def f_ejecutar_consulta_a_tabla (conexion, comando):
    cursor = conexion.cursor()
    resultado = None
    try:
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for cli in resultado:
            print(cli)
        return resultado
    
    except Error as e:
        print(f" Ocurrio el error '{e}' al ejecutar el comando '{comando}'")         
    

def f_cargar_clientes(fila):
    nit=fila['NIT']
    cliente=fila['Cliente']
    comando="""select * from clientes where nit = ?"""
    resultado = ejecutar_consulta_un_registro(conexion,comando, (nit,))
    if resultado==None:
       print(f'{nit} nuevo')
       comando="""insert into clientes (nit, nombres) values (?,?)"""
       ejecutar_comando_sql(conexion, comando, (nit,cliente))
    
def f_cargar_productos(fila):
    codProducto = fila['CodigoProducto']
    codCorto = codProducto[len(codProducto)-7:]
    descProducto = fila['DescProducto']
    comando="""select * from productos where id_producto = ?"""
    resultado = ejecutar_consulta_un_registro(conexion,comando, (codCorto,))
    if resultado==None:
       print(f'{codCorto} nuevo')
       comando="""insert into productos (id_producto, descripcion) values (?,?)"""
       ejecutar_comando_sql(conexion, comando, (codCorto,descProducto))
    
def f_cargar_facturas(fila):
    nit=fila['NIT']
    tipoDocto = fila['TipoDocto']
    documento = fila ['Documento']
    fecha=fila['Fecha']
    descripcion="FAC"
    comando="""select * from facturas where id_documento = ? and descripcion = ?"""
    resultado = ejecutar_consulta_un_registro(conexion,comando, (documento,descripcion))
    if resultado==None:
       print(f'{documento} nuevo')
       comando="""insert into facturas (id_documento, descripcion, fecha, valor, nit) values (?,?,?,?,?)"""
       ejecutar_comando_sql(conexion, comando, (documento,descripcion, fecha, 0.0, nit))
def f_cargar_ventas(fila):
    """
        id_documento CHAR(12) NOT NULL,
        id_producto CHAR(12) NOT NULL,
        fecha timedate,
        cantidad DECIMAL,
        valor DECIMAL,
        costo DECIMAL,
        PRIMARY KEY (id_documento, id_producto)
        FOREIGN KEY (id_producto) REFERENCES productos (id_producto)
        FOREIGN KEY (id_documento) REFERENCES facturas (id_documento)
    """
    documento = fila ['Documento']
    codProducto = fila['CodigoProducto']
    codCorto = fila['CodigoProducto'][len(fila['CodigoProducto'])-7:]
    print(f'Es {codProducto} == {codCorto}')
    fecha=fila['Fecha']
    cantidad=int(fila['Cantidad'])
    precioUnitario = int(fila['Precio Unitario'])
    totalDetalle = int(fila['Total Detalle'])
    costoUnitario = int(fila['Costo Vigente'])
    
    datos_insertar=(documento,codCorto,fecha,cantidad,precioUnitario,costoUnitario)
    
    comando="""insert into ventas (
        id_documento,id_producto, fecha, cantidad, valor, costo) values (?,?,?,?,?,?)"""
    ejecutar_comando_sql(conexion, comando, datos_insertar)

#### Se conecta a la base de datos. Si no existe, la crea vacía

conexion=crear_conexion(nombreDB)

with open (csv_fn,'r') as fn:  #  Se define contexto para el proceso siguiente
    lector = csv.DictReader(fn)          #  Objeto lector con el método reader de csv
    
    for fila in lector:  
        nit=fila['NIT']
        cliente=fila['Cliente']
        tipoDocto = fila['TipoDocto']
        documento = fila ['Documento']
        fecha=fila['Fecha']
        codProducto = fila['CodigoProducto']
        codCorto = codProducto[len(codProducto)-7:]
        descProducto = fila['DescProducto']
        cantidad=int(fila['Cantidad'])
        precioUnitario = int(fila['Precio Unitario'])
        totalDetalle = int(fila['Total Detalle'])
        costoUnitario = int(fila['Costo Vigente'])
        f_cargar_clientes(fila)
        f_cargar_productos(fila)
        f_cargar_facturas(fila)
        f_cargar_ventas(fila)
    
    comandos = []    
    comandos.append("""select * from clientes order by nombres""")
    comandos.append("""select * from productos order by id_producto""")
    comandos.append("""select * from facturas""")
    comandos.append("""select * from ventas""")
    
    for comando in comandos:
        print(f' ejecutando  {comando}')
        print(f'{"=" * (len(comando) + 15)}')
        f_ejecutar_consulta_a_tabla(conexion,comando)
    