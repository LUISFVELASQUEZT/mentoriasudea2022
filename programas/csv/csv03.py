import csv

csv_local_fn = "../mentoriasudea2022/data/datos.csv"

#### Lectura de archivos .CSV con el método DictReader

with open (csv_local_fn,'r') as fn:  #  Se define contexto para el proceso siguiente
    lector = csv.DictReader(fn)          #  Objeto lector con el método reader de csv
    
    for fila in lector:              #  Iterar sobre las líneas 2 a la n-1
        
        print(f" La cedula {fila['Cedula']} corresponde a {fila['Nombres']} {fila['Apellidos']}")
        
    print(f"Total registros {lector.line_num-1}")





    
    
