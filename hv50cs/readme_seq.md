Datos tipo secuencia en Python.

- list (listas), tuple (tuplas) y range (rangos) son los tres tipos básicos de secuencias.
- las listas son sencuencias mutables. 

Las secuencias soportan operaciones comunes:

- x in s True si el elemento x está en la secuencia s, False si el elemento x no está en s

    Ejemplo 01:

    s = ["Pedro", "Luis", "Diego"]

    x = "Luis"
    y = "Juan"

    if x in s:                            ###  es True
        print(f" {x} está en la lista")   ### se imprimiría esta línea
    else:
        print(f" {x} NO está en la lista")

    if y in s:                            ### es False
        print(f" {y} está en la lista")
    else:
        print(f" {y} NO está en la lista")   ### se imprimiría esta línea



- x not in s True si el elemento x no está en la secuencia s, False si x está en s

Ejemplo 02:

    s = ["Pedro", "Luis", "Diego"]

    x = "Luis"
    y = "Juan"

    if not x in s:                          ### False
        print(f" {x} NO está en la lista")
    else:
        print(f" {x} está en la lista")     ### se imprimiría esta línea

    if not y in s:                           ### es True
        print(f" {y} NO está en la lista")   ### se imprimiría esta línea
    else:
        print(f" {y}  está en la lista")   


    Copia el Ejemplo 02 y prueba 

- s + t : concatenación 

    Ejemplo 03:

    s = ["Bogotá","Caracas","Quito","Lima","Sucre"]
    t = ["Santiago","Buenos Aires","Montevideo","Asunción","Brasilia"]

    capitales = s + t

    print(f" Lista 1 de capitales: {s}")
    print(f" Lista 2 de capitales: {t}")
    print(f" Lista completa de capitales: {capitales}")

- s * n or n * s  repetición n veces de una secuencia

    Ejemplo 04

    s = ["a","e","i","o","u"]
    r = s * 3

    print (f" Las vocales una vez {s}")
    print (f" Las vocales repetidas 3 veces: {r}")

Ejemplo 05: acceder al elemento que ocupa una posición i en la lista 

- s[i] acceder al elemento que ocupa la posición i en una lista (numerados desde 0)
- El índice i puede variar entre 0 y la longitud de la lista - 1. En este caso de 0 a 4.

    vocales = ["a","e","i","o","u"]

    una_vocal = vocales[0]

    print(f"Vocales {vocales}")
    print(f"Vocales {una_vocal}")

Ejemplo 6

- Encontrar un elemento por su índice, protegiendo el programa de un índice equivocado.
- En este ejemplo el índice solicitado varía entre 1 y 5. 
- Al ingresar un valor fuera del rango el programa termina. Mientras tanto, itera pidiendo
-  un índice y desplegando la vocal correspondiente.
    
## Ejemplo 6

vocales = ["a","e","i","o","u"]

while True:
    try:
        ix= int(input(" Indique el número de vocal que desea: "))
        su_vocal = vocales[ix-1]
        print (f"Ud solicito la vocal numero {ix} : {su_vocal}")
    except:
        print("Lo siento. Solo son 5 vocales")
        break


- Slices. Una forma de acceder parcialmente o totalmente a los elementos de una lista es mediante los slices.
-         s[i:j:k]  se toma un slice de la secuencia s, desde el elemento i hasta el j-1 cada k elementos.
-         tanto i, como j, como k pueden omitirse.
Ejemplo 7. 
    # 7.1. vocales[i:j:k]     donde i es el índice inicial, j el final, y k el incremento.
    # 7.2. vocales[i:j]       si se omite la k, se avanza de 1 en uno
    # 7.3. vocales[i:] o 7.4. vocales[i::k]  si se omite la j, avanza hasta el final
    # 7.5. vocales[:]  o 7.6. vocales[:j:k]     o 7.7. vocales[:j] si se omite la i, se toma desde el principio

    vocales = ["a","e","i","o","u"]

    print(vocales[0:4])          ### imprime desde i=0 hasta k-1 de 1 en uno : a,e,i,o

- len(s)    obtiene la longitud (el número de elementos) que contiene una secuencia

- min(s)     muestra el elemento cuyo valor sea el menor.
             En el caso de textos sería el texto que ocupa el primer lugar al ordenar alfabéticamente.

- max(s)     muestra el elemento cuyo valor sea el mayor.
             En el caso de textos sería el texto que ocupa el último lugar al ordenar alfabéticamente. 

Ejemplo: las listas people y more_people contienen nombres de personas
             la lista all_people contiene la concatenación de people y more_people.

    people = ["Luis","Carlos","Myriam","Tatiana","Sofia","Fernando","Sofia"]
    more_people = ["Sandra","Sebastian","Jorge","Carolina","Jose","Sofia"]
    all_people = people + more_people

    print(f"En People hay {len(people)} nombres, desde {min(people)} hasta {max(people)} ")
    print(f"En People hay {len(more_people)} nombres, desde {min(more_people)} hasta {max(more_people)} ")



    print(f"Unidos son {len(all_people)} nombres, desde {min(all_people)} hasta {max(all_people)} ")


- count(s)   Cuenta las veces que un valor aparece en una secuencia

Ejemplo:

    buscar = "Carlos"

    print(f"{buscar} figura {all_people.count(buscar)} vez/veces.")


Ejemplo: data una lista con nombres de personas mostrar el nombre que figura más veces. De haber varios, muestra el último que encuentre.

    max=0           ## número de veces que figura el nombre que está en who
    who=""          ## nombre que figura más veces

    for _ in all_people:
        cnt = all_people.count(_)
        who = _
        if  cnt > max:
            max = cnt
            who = _

    print(f"{who} está {cnt} veces.")

- s.index(x[, i[, j]]) Index: obtiene la posición donde aparece un valor x en la secuencia s.
            Si se incluye i, la búsqueda se inicia en esa posición.
            Si se incluye j, se busca cada j elementos.
Ejemplo:
    
    who="Jorge"
    print(all_people.index(who))   ## muestra la posición ocupada por el "Jorge"
    ix=all_people.index(who)
    who=all_people[ix+1]           ## ubica el nombre que ocupa la posición siguiente
    print(who)                     ## muestra el nombre obtenido


- sorted : permite ordenar una secuencia, orden ascendente o descendente

Ejemplo:

    print("Orden ascendente ")

    for _ in (sorted(all_people, reverse=False)):
        print(f"{_}, ",end="")

    print("\nOrden descendente ")

    for _ in (sorted(all_people, reverse=True)):
        print(f"{_} ,",end="")
    print()


- copiado de listas

    - al copiar con método copy o con un slice se obtienen listas independientes, que son diferentes objetos.
    - Al actualizar alguna no se afecta la otra.
    - Ver ejemplos 01 y 03.
    - al copiar con copia_lista = lista_original se obtienen dos referencias al mismo objeto. Ver ejemplo 02

    - el archivo que contiene el código Python es list_copy.py

        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

        copy_colors = colors[:]   ###################### son dos listas independientes
        print("=============Ejemplo 01 ==============================================")
        print("              Dos listas independientes, colors : ", colors)
        print("y copy_color copiados así:copy_colors = colors[:] ",copy_colors)
        print("===========================================================")
        colors.pop()               # elimina el último valor de colors, copy_colors lo mantiene

        print("colors después del pop: >>>>>>>>",  colors)
        print("copy_Colors después del pop: >>>",  copy_colors,"\n")

        print("========= Ejemplo 02 ==================================================")
        print(" Dos nombres de listas, son el mismo objeto")
        print("===========================================================")
        copia = colors            # tienen diferente nombre pero la misma referencia
        print("lista copia  : ", copia)
        print("lista colors : ",colors)

        print("Agregando gray a copia: ")
        copia.append('gray')
        print("Copia Colors también refleja el valor agregado", copia)    ### colors y copia son el mismo objeto
        print("      Colors también refleja el valor agregado", colors, "\n")
        print("=======Ejemplo 03 ====================================================")
        print(" Dos ejemplares independientes al copiar con el método copy: ")
        print("===========================================================")
        copia2 = colors.copy()   ### copia independiente del original
        copia2.pop()
        print("colors mantiene el contenido original ", colors)
        print("copia2 no tiene el elmento elimnado   ", copia2)