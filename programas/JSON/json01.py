import json

json_fn = "../mentoriasudea2022/data/marvel.json"   #   Ruta al archivo json con los datos.

clave_gen = "Cinemateca Marvel"   #   Clave principal de búsqueda por cinemateca
clave_pel = 'Iron Man'            #   Clave de búsqueda de película

def f_trazo(texto):
    print(f"{'<'*int(len(texto)/2)} {'>'*int(len(texto)/2)}")
    print(f"{texto}")
    print(f"{'<'*int(len(texto)/2)} {'>'*int(len(texto)/2)}")

with open(json_fn) as marvel:
    
    data=json.load(marvel)
    texto = "01. Datos cargados de json"
    f_trazo("BEGIN " + texto)
    print(f"{type(data)} >> {data[clave_gen][clave_pel]}")
    f_trazo("END " + texto)

texto = " 02. Datos de peliculas"
f_trazo("BEGIN " + texto)  
#for peli in data[clave_gen]:
for peli in data:
    
    print(f" 02. Datos {type(peli)} de peliculas {peli}")

f_trazo("END " + texto) 

texto = " 03. Datos de peli {type(peli)} contienen {peli}"
f_trazo("BEGIN " + texto)

for peli in data[clave_gen]:
  print(f" 03. Datos de peli {type(peli)} >> {peli}")

f_trazo("END " + texto)

datos_peli = data[clave_gen][clave_pel]
texto=" 04. Detalle de {clave_gen} : {clave_pel} {type(datos_peli)}"
f_trazo("BEGIN " + texto)
print(f" 04. Detalle de {clave_gen} : {clave_pel} {type(datos_peli)}")
f_trazo("END " + texto)

texto=" 05. {det} : {datos_peli[det]} es  {type(det)}"
f_trazo("BEGIN " + texto)

for det in datos_peli:
    
    print(f" 05. {det} : {datos_peli[det]} es {type(det)}")
f_trazo("END " + texto)

texto=" 06. Otro detalle {type(datos_peli)} = {datos_peli}"
f_trazo("BEGIN " + texto)
print(f" 06. Otro detalle {type(datos_peli)} = {datos_peli}")
f_trazo("END " + texto)

texto=" 07. Claves de "
f_trazo("BEGIN " + texto )

for det_peli in data[clave_gen][clave_pel]:
    print(f" 07. {det_peli} : {data[clave_gen][clave_pel][det_peli]}")
f_trazo("END " + texto)

with open(json_fn) as marvel:
    
    data=json.load(marvel)
    for cin in data:
      print("Cin " + cin)
      for pel in data[cin]:
        texto=cin + " ****" + " Pelicula: " + pel
        f_trazo(texto)
        for det in data[cin][pel]:
            print(f' >>>> {det} = {data[cin][pel][det]}')
        f_trazo( " Fin de >>> " + texto)
        f_trazo(texto="")