# csv1180.py
#
# 

import csv
csv_local_fn = "mlb_players.csv"

datos = []

with open (csv_local_fn,'r') as fn:  #  Se define contexto para el proceso siguiente
    lector = csv.DictReader(fn)   #  Objeto lector con el método reader de csv
    for fila in  lector:                
        print(f"{fila['Name']} {fila['Position']}{fila['Team']} {fila['Height(inches)']} \
             {fila['Weight(lbs)']} {fila['Age']}")
                
                                                         
        
    print(f"Total registros {lector.line_num}")
    


