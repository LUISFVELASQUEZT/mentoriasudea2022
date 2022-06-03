# csv01.py

# 

import csv

csv_copia  = "mentoriasudea2022\data\copia.csv"
csv_local_fn = "mentoriasudea2022\data\datos.csv"


cabecera = []
datos = []

with open (csv_local_fn,'r') as fn:  #  Se define contexto para el proceso siguiente
    lector = csv.reader(fn)          #  Objeto lector con el método reader de csv
    cabecera = next(lector)          #  Se lee la primera linea del archivo .csv y se asigna a cabecera
    for fila in lector:              #  Iterar sobre las líneas 2 a la n-1   
                        
        if (int(fila[5]) < 75):
            datos.append(fila)          #  Agrega la línea a la lista datos
            print(f"La cédula {fila[0]} corresponde a {fila[1]}  {fila[2]} y su peso es {fila[5]} kgs")   # fila es una lista con  campos (o a 7)
        
    print(f"Total registros {lector.line_num}")
print(f"Encabezado : {cabecera}")
  
    
#  Copiar datos

with open(csv_copia,'w') as fn_copia:
    escritor = csv.writer(fn_copia)
    escritor.writerow(cabecera)
    escritor.writerows(datos)

with open(csv_copia,'r') as fn_copia_l:
    print(fn_copia_l.read())