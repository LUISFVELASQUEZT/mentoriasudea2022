import pandas as pd

estudiantes = {
            'Cedula1':    {'Nombre': 'Carlos Alberto', 'Edad': 35, 'Ciudad': 'Monteria'},
            'Cedula2':    {'Nombre': 'Rodrigo', 'Edad': 31, 'Ciudad': 'Envigado'},
            'Cedula3':    {'Nombre': 'Luis Fernando', 'Edad': 33, 'Ciudad': 'Cali'},
            'Cedula4':    {'Nombre': 'María Luisa', 'Edad': 23, 'Ciudad':  {  'sede': 'Bogota', 
                                                                'actual': 'Pereira'
                                                                }},
            }

df = pd.DataFrame(estudiantes).T

print(df)

df = pd.DataFrame(estudiantes)
print(df)