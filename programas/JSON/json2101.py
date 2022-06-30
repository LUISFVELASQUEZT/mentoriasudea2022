# json : javascript objetc notation

import json

### datos_alumnos es un string con un formato json valido
#### semeja un diccionario de Python
#### alumnos es un arreglo de tres objetos
### cada objeto contiene varias claves:
###  nombres, apellidos, cedula, telefono , genero, lenguajes , ciudad, idiomas

datos_alumnos = '''
{                           
    "alumnos": [           
        {                   
            "nombres": "Juan Carlos",
            "apellidos": "Perez Ochoa",
            "cedula": "12.123.456",
            "telefono": "315-6088686",
            "genero": "masculino",
            "email": "jcarlos@gmail.com",
            "bilingue":false,
            "ciudad": "Pasto",
            "lenguajes":["Python","Java"]
            
        },
        {
            "nombres": "Luis Fernando",
            "apellidos": "Ortiz Tobón",
            "cedula": "12.123.777",
            "telefono": "315-6789009",
            "genero": "masculino",
            "email": "jfortiz@gmail.com",
            "bilingue":true,
            "ciudad": "Caldas",
            "lenguajes":null
        },
        {
            "nombres": "Martha Lucia",
            "apellidos": "Salazar Ortiz",
            "cedula": "12.444.678",
            "telefono": "315-9908989",
            "genero": "femenino",
            "email": "mlsalazar@gmail.com",
            "bilingue":false,
            "ciudad": "Mitu",
            "lenguajes":["Python","Java","JavaScript"]
        }
    ]
}
'''

## para manipularlo se almacena este string de python en un objeto Python

datos = json.loads(datos_alumnos)

# JSON conversion to Python:

## JSON OBJECT >>>>>>  Python dict
## JSON Array >>>>>>   Python list
## JSON String >>>>>>  Python string
## JSON Integer >>>>>> Python int
## JSON Real >>>>>>    Python float
## JSON true >>>>>>    Python True
## JSON false >>>>>>   Python False
## JSON null >>>>>>    Python None

for dato in datos['alumnos']:
    print(dato['nombres'],dato['ciudad'],dato['bilingue'],dato['lenguajes']) 
    
# Eliminar la variable "bilingue" y guardar en un string json

for dato in datos['alumnos']:
    del dato['telefono']
    
nuevos_datos = json.dumps(datos, indent=3, sort_keys=True)
print(nuevos_datos)
