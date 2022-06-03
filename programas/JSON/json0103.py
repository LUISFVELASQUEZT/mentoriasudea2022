import json

json_fn = "mentoriasudea2022\data\personal.json"
clave_gen = ""
clave_dep = ''

with open(json_fn) as personal:
    
    data=json.load(personal)
    print(type(data),data)

for empresa in data:
    print(type(empresa),empresa)


datos_empre = data[clave_gen][clave_dep]

print(f"{clave_gen} : {clave_dep} {type(datos_empre)}")

for det in datos_empre:
    
    print(f"{det} : {datos_empre[det]} {type(det)}")

print(type(datos_empre),datos_empre)
    
for empresa in data[clave_gen][clave_dep]:
    print(f"{empresa} : {data[clave_gen][clave_emp][empresa]}")