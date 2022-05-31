myDicti1 = {'key1' : 'value1', 'key2' : 'value2'}

myDicti2 = {'key11' : 'value11', 'key12' : 'value12'}

print(f" El {type(myDicti1)}, contiene {myDicti1} con {len(myDicti1)} elementos.")
print(f" El {type(myDicti2)}, contiene {myDicti2} con {len(myDicti2)} elementos.")
print(type(myDicti2),myDicti2)

myDicti1.update(myDicti2)

print(f" Y ahora el {type(myDicti1)}, contiene {myDicti1} con {len(myDicti1)} elementos.")

myDicti2['clave30'] = 'valor30'

print(f" El {type(myDicti2)}, contiene {myDicti2} con {len(myDicti2)} elementos.") 

clave40='clave40'
valor40='valor40'

myDicti2[clave40] = valor40

print(f" El {type(myDicti2)}, contiene {myDicti2} con {len(myDicti2)} elementos.") 

