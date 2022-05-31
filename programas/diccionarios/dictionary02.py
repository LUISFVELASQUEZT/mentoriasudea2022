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
    

print(myDictionary)
    