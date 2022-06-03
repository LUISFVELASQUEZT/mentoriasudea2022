# csv01def.py
# by luisvelasquezt@protonmail.com
# 2022
# mentorias u de a
# 

import csv

csv_copia  = "mentoriasudea2022\data\copia.csv"
csv_local_fn = "mentoriasudea2022\data\datos.csv"

cabecera = []
datos = []

def f_reader_csv(peso):
    with open (csv_local_fn,'r') as fn:  #  Se define contexto para el proceso siguiente
      lector = csv.reader(fn)          #  Objeto lector con el método reader de csv
      cabecera = next(lector)          #  Se lee la primera linea del archivo .csv y se asigna a cabecera
      for fila in lector:              #  Iterar sobre las líneas 2 a la n-1   
                        
        if (int(fila[5]) < peso):
            datos.append(fila)          #  Agrega la línea a la lista datos
            print(f"La cédula {fila[0]} corresponde a {fila[1]}  {fila[2]} y su peso es {fila[5]} kgs")   # fila es una lista con  campos (o a 7)
        
    print(f"Total registros {lector.line_num}")
    print(f"Encabezado : {cabecera}")
   
#  Copiar datos

def f_copia():
    with open(csv_copia,'w') as fn_copia:
        escritor = csv.writer(fn_copia)
        escritor.writerow(cabecera)
        escritor.writerows(datos)

def f_print_copia():
    with open(csv_copia,'r') as fn_copia_l:
         print(fn_copia_l.read())
         
def f_trazo(texto):
    print(f"{'<'*int(len(texto)/2)} {'>'*int(len(texto)/2)}")
    print(f"{texto}")
    print(f"{'<'*int(len(texto)/2)} {'>'*int(len(texto)/2)}")

texto="Paso 1: leyendo .csv e imprimiendo con selección"
f_trazo(texto)      
f_reader_csv(100)
texto="Paso 2: copiando .csv"
f_trazo(texto)
f_copia()
texto="Paso 3: imprimiendo la copia .csv"
f_trazo(texto)
f_print_copia()