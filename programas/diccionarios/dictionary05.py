import json as json

estudiantes = {
            'Cedula1':    {'Nombre': 'Carlos Alberto', 'Edad': 35, 'Ciudad': 'Monteria'},
            'Cedula2':    {'Nombre': 'Rodrigo', 'Edad': 31, 'Ciudad': 'Envigado'},
            'Cedula3':    {'Nombre': 'Luis Fernando', 'Edad': 33, 'Ciudad': 'Cali'},
            'Cedula4':    {'Nombre': 'María Luisa', 'Edad': 23, 'Ciudad':  {  'sede': 'Bogota', 
                                                                'actual': 'Pereira'
                                                                }},
            }

print(json.dumps(estudiantes, indent=4))
