import json

clave_gen = 'Cinemateca Marvel'
clave_pel = 'The Incredible Hulk'

with open   ("mentoriasudea2022\data\marvel_b.json") as marvel:
    
    data=json.load(marvel)
    
for peli in data:
   box_size = len(peli) +4
   print("="*box_size)
   print(f"  {peli.upper()}  ")
   print("="*box_size)
   clave_gen=peli
   for peli in data[peli]:
        to_print=len(peli) + len(clave_gen)+12
        print(f"Pelicula {peli} en {clave_gen}")
        print("<" * to_print)
        datos_peli = data[clave_gen][peli]
        for det in datos_peli:
            print(f"{det} : {datos_peli[det]}")