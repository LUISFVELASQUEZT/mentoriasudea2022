import csv

csv_fn = "../mentoriasudea2022/data/prueba3NF.csv"

def f_cargar_clientes(a,b):
    pass
def f_cargar_productos(a,b,):
    pass
def f_cargar_facturas(a,b,c,d):
    pass
def f_cargar_ventas(a,b,c,d):
    pass

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
        print(f'Nit: {nit} es {cliente} Doc: {tipoDocto}-{documento} {fecha} {codProducto} {codCorto} {descProducto} {cantidad} {precioUnitario} {totalDetalle} {costoUnitario}')
        f_cargar_clientes(nit,cliente)
        f_cargar_productos(codCorto, descProducto)
        f_cargar_facturas(tipoDocto,documento, nit,fecha )
        f_cargar_ventas(tipoDocto,documento, nit,fecha)
        
       
    


    
    
