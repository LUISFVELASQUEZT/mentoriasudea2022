# csv03def.py
# by luisvelasquezt@protonmail.com
# 2022
# mentorias u de a
# 

import csv

csv_copia  = "mentoriasudea2022\data\copia.csv"
csv_local_fn = "mentoriasudea2022\data\datos.csv"


datos = []

def f_reader_csv(peso):
    with open (csv_local_fn,'r') as fn:  #  Se define contexto para el proceso siguiente
      lector = csv.DictReader(fn)          #  Objeto lector con el método DictReader de csv
                
      for fila in lector:              #  Iterar sobre las líneas 2 a la n-1   
        if (int(fila['Peso'])<peso):                
          print(f" La cedula {fila['Cedula']} corresponde a {fila['Nombres']}: {fila['Apellidos']} peso {fila['Peso']} kgs.")
        
    print(f"Total registros {lector.line_num}")
    
#  Copiar datos

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})



def f_copia():
    with open(csv_copia,'w',newline='') as fn_copia:
        field_names = ['Cedula','Nombres','Apellidos','Peso','Edad']
        escritor = csv.DictWriter(fn_copia,fieldnames=field_names)
        escritor.writerow({'Cedula': 1010, 'Nombres': 'Pedro','Apellidos':'Páramo','Peso':87,'Edad':66})
        escritor.writerow({'Cedula': 2020, 'Nombres': 'Antonio','Apellidos':'Salazar','Peso':77,'Edad':56})
def f_print_copia():
    with open(csv_copia,'r') as fn_copia:
         print(fn_copia.read())
         
def f_trazo(texto):
    print(f"{'<'*int(len(texto)/2)} {'>'*int(len(texto)/2)}")
    print(f"{texto}")
    print(f"{'<'*int(len(texto)/2)} {'>'*int(len(texto)/2)}")

texto="Paso 1: leyendo .csv e imprimiendo con selección"
f_trazo(texto)      
f_reader_csv(80)
texto="Paso 2: copiando .csv"
f_trazo(texto)
f_copia()
texto="Paso 3: imprimiendo la copia .csv"
f_trazo(texto)
f_print_copia()