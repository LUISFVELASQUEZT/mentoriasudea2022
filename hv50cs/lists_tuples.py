import random

people = ["Luis","Carlos","Myriam","Tatiana","Sofia","Fernando"]
more_people = ["Sandra","Sebastian","Jorge","Carolina","Jose"]

persons = []   

def main():
    
    prueba_listas()

def list_append():
                     ## así definimos una lista vacía
    persons.append("Luis")          ## append es un método de la clase list
    persons.append("Carlos")        ##   agrega al final de la lista
    persons.append("Myriam")
    persons.append("Tatiana")
    persons.append("Sofia")

    
    imprime_encabezado(" 1. Lista persons, una a una",persons,1)

    for person in persons:             ## iteramos sobre la lista persons y recibimos los datos en person
        print(f" {person}", end="" )   ## imprimimos el nobre de cada person
    print("\n")                                
    
    imprime_encabezado(" 2. Lista persons: lista completa",persons,4)
        
    print(persons)

def list_slice():
    pass

def imprime_encabezado(texto, list_or_tuple, inc=1):
    nchar = 0
    for _ in list_or_tuple:
        nchar += len(_) + inc

    print("=" * nchar)
    print(texto)
    print("=" * nchar)
    
  
def prueba_listas():

    list_append()

    imprime_encabezado(" 3. Slice desde 1 ",persons[1::],1)

    for person in persons[1::]:
        print(f' {person}', end="")
    print("\n") 

    persons2 = list()

    for person in persons:
        persons2.append(person)       ##  copia la lista item a item 

    persons2.insert(2,"Fernando")     ## inserta Fernando en índice 2

    imprime_encabezado(" 4. Copia, inserta, elimina (pop y remove ",persons2,1)

    for person in persons2:
        print(f" {person}", end="")

    print("\n")
    
    fuera=persons2.pop()                         #  Elimina al último, como en un stack.

    print(f" Salio {fuera} quedaron {persons2}")

    alguien = random.choice(people)              ## elige al azar alguien a quien retirar. 
    
    print(f" Saliendo {alguien}")
  
    
    try:                                         ## Retira al elegido al azar, si no fue retirado con el pop anterior
        persons2.remove(alguien)
        print(f" Quedaron {persons2}")
        imprime_encabezado(" 4. Quedaron ",persons2,1)
    except:
        print(f" Error al tratar de retirar a {alguien}")
        
    print(f"5. Asi estamos :  {persons}")          ## Muestra como quedó la lista
    persons3 = sorted(persons)                     ## Ordena la lista en una nueva persons3
    print(f"Asi quedamos :  {persons3}")           ## Muestra como quedó la lista ordenada

    imprime_encabezado((" 6- Orden ascendente " + str(len(people) + len(more_people))),(people + more_people),4)
    print()
    i = 0
    for person in sorted(people + more_people):    ##  concatea las dos listas y las ordena
        i+=1
        print(f"{i:02} {person} ",end="")
    print()
    imprime_encabezado((" 6- Descendente " + str(len(people) + len(more_people))),(people + more_people), 4)
    
    i = 0
    
    for person in sorted(people + more_people,reverse=True):
        i+=1
        print(f"{i:02} {person} ",end="")
    

if __name__ == "__main__":
    main()