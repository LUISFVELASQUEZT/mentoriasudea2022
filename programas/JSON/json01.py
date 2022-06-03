import json

#from matplotlib.font_manager import json_load

json_fn = "mentoriasudea2022\data\marvel.json"   #   Ruta al archivo json con los datos.

clave_gen = "Cinemateca Marvel"   #   Clave principal de búsqueda por cinemateca
clave_pel = 'Iron Man'            #   Clave de búsqueda de película

with open(json_fn) as marvel:
    
    data=json.load(marvel)
    print(f" 01. Datos {type(data)} cargados de json {data}")

for peli in data:
    print(f" 02. Datos {type(peli)} de peliculas {peli}")


for peli in data[clave_gen]:
  print(f" 03. Datos de peli {type(peli)} contienen {peli}")

datos_peli = data[clave_gen][clave_pel]

print(f" 04. Detalle de {clave_gen} : {clave_pel} {type(datos_peli)}")

for det in datos_peli:
    
    print(f" 05. Detalle de dato  {det} : {datos_peli[det]} {type(det)}")

print(f" 06. Otro detalle {type(datos_peli)} = {datos_peli}")
    
for peli in data[clave_gen][clave_pel]:
    print(f" 07. {peli} : {data[clave_gen][clave_pel][peli]}")
