# csv1180.py
#
# 

import csv
csv_local_fn = "../mentoriasudea2022/data/DummySalesData.csv"

datos = []

with open (csv_local_fn,'r') as fn:  #  Se define contexto para el proceso siguiente
    lector = csv.DictReader(fn)   #  Objeto lector con el método reader de csv
    for fila in lector:     
          print(f'{fila["OrderID"]}  {fila["Product_Code"]} \
                {fila["Quantity"]} {fila["UnitPrice(USD)"]} {fila["Sales_Manager"]}')                                          
        
    print(f"Total registros {lector.line_num}")
    


