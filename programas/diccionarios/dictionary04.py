estudiantes = {
            'Cedula1':    {'Nombre': 'Carlos Alberto', 'Edad': 35, 'Ciudad': 'Monteria'},
            'Cedula2':    {'Nombre': 'Rodrigo', 'Edad': 31, 'Ciudad': 'Envigado'},
            'Cedula3':    {'Nombre': 'Luis Fernando', 'Edad': 33, 'Ciudad': 'Cali'},
            'Cedula4':    {'Nombre': 'María Luisa', 'Edad': 23, 'Ciudad':  {  'sede': 'Bogota', 
                                                                'actual': 'Pereira'
                                                                }},
            }


def print_dict_anidado(dict_obj, indent = 0):
    ''' Pretty Print nested dictionary with given indent level  
    '''
    # Iterate over all key-value pairs of dictionary
    for key, value in dict_obj.items():
        # If value is dict type, then print nested dict 
        if isinstance(value, dict):
            print(' ' * indent, key, ':', '{')
            print_dict_anidado(value, indent + 4)
            print(' ' * indent, '}')
        else:
            print(' ' * indent, key, ':', value)
def display_dict(dict_obj):
    ''' Pretty print nested dictionary
    '''
    print('{')
    print_dict_anidado(dict_obj, 4)
    print('}')
display_dict(estudiantes)
















claves = ['clave1','clave2','clave3','clave4','clave5']
valores = ['valor1','valor2','valor3','valor4','valor5']

myDictionary = {}

for clave in claves:
    print(f" La clave es {clave}")
    
for valor in valores:
    print(f" El valor es {valor}")
clave=""
valor=""
print(range(len(claves)))
for x in range(len(claves)):
    clave=claves[x]
    valor=valores[x]
    myDictionary[clave]=valor
    
for key, value in myDictionary.items():
    print(f"El contenido de {key}, es :, {value} .")
    

print(myDictionary)
    