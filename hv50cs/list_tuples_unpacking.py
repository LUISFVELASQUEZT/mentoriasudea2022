colores = ['rojo', 'naranja', 'amarillo', 'verde', 'azul', 'indigo', 'violeta']

colores_en_tupla = tuple(colores)
print("====================================")
print ("Paso 1 colores        " ,colores)
print("Paso 2 colores_en_tupla", colores_en_tupla)
print("====================================")

color1, *color2, color3 = colores   ## unpacking de color1, ultimo color, demás colores

print(f" Desempacados de lista")
print(f" : primero, ultimo, resto >>")
print(f" Color1 {color1} color último >> {color3}  resto >>> {color2}")

color1, *color2, color3 = colores_en_tupla
print("====================================")
print(f" Desempacados de tupla :")
print(f" primero, ultimo, el resto")
print(f"Color1 {color1} color último {color3}  resto {color2}")
print("====================================")
mi_tupla = tuple(colores)

print(" Impresión de colores en tupla, ordenados por color: ")
for color in sorted(mi_tupla):
    print(f'{color} ', end="")
print("\n")
print(f"Slice de tuplas: desde len(mi_tupla) hacia atrás de 1 en uno]")
print(f"Mi tupla {mi_tupla}")
print(f"     len {mi_tupla[len(mi_tupla)::-1]}")


print("====================================")
print(f"Slice de mi tupla desde el final cada tercero: {mi_tupla[7::-3]}")
print("====================================")

# lista que contiene listas anidadas

lista = [["Colombia",["Bogota",8500000]],["Chile",["Santiago",8000000]],
         ["Venezuela",["Caracas",7000000]],["Argentina",["Buenos Aires",6000000]]
]


## unpacking de lista ordenada por país, que contiene como elementos listas 

for par in sorted(lista):
    pais, capital = par     ## primer unpacking de pais y lista de capital
    ciudad, poblacion = capital   ## de la lista capital unpacking de ciudad y población
    print(f"La capital de {pais} es {ciudad}, ciudad con {poblacion} habitantes." )