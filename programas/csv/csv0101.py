import csv

csv_local_fn = "mentoriasudea2022\data\datos.csv"
csv_copia = "mentoriasudea2022\data\.csv"


cabecera = []
datos = []

with open (csv_local_fn,'r') as fn:  #  Se define contexto para el proceso siguiente
    lector = csv.reader(fn)          #  Objeto lector con el método reader de csv
    cabecera = next(lector)          #  Se lee la primera linea del archivo .csv y se asigna a cabecera
    for fila in lector:              #  Iterar sobre las líneas 2 a la n-1
        datos.append(fila)           #  Agrega la línea a la lista datos
        print(f"La cédula {fila[0]} corresponde a {fila[1]}  {fila[2]}")   # fila es una lista con  campos (o a 7)
        
    print(f"Total registros {lector.line_num-1}")


#  Copiar datos

with open(csv_copia,'w') as fn_copia:
    salida = csv.writer(fn_copia)
    salida.writerow(cabecera)
    salida.writerows(datos)

    
    
