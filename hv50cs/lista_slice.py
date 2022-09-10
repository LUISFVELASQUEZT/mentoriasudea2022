"""
    Ejemplos elaborados por LuisVelasquezT
    luisvelasquezt@pm.me
    luisvelasquezt@gmail.com
    como material de apoyo para talleres y  mentorías
    en python.
    2022 
    Pueden usarse libremente

"""
def main():

    s = ["a","e","i","o","u"]
    r = s * 3
    
    ## Ejemplo 5 

    vocales = ["a","e","i","o","u"]

    una_vocal = vocales[0]

    print(f"Vocales            ==>> {vocales}")
    print(f"Una vocal          ==>> {una_vocal}")
    r = s * 3
    print(f"Repetición 3 veces ==>> {r}\n")

    ## Ejemplo 6

    print(f"Ejercicio con selección de vocal\n")

    while True:
        try:
            ix= int(input(" Indique el número de vocal de 1 a 5 o 6  para finalizar: "))
            if ix < 1:
                raise ValueError
            su_vocal = vocales[ix-1]
            print (f"Ud solicito la vocal numero {ix} : {su_vocal}")
        except:
            print("Lo siento. Solo son 5 vocales")
            break

    ## Ejemplo 7


    vocales = ["a","e","i","o","u"]

    print(f"\nEjemplo 7: La lista vocales contiene ==> {vocales[:]} y se usa para estos ejemplos. \n")

    print(f"Ejemplo 7.1. : s[i:j:k] => vocales[0:4:2] resultado ==> {vocales[0:4:2]}")  

    print(f"Ejemplo 7.2. : s[i:j]   => vocales[0:4]   resultado ==> {vocales[0:4]}")  

    print(f"Ejemplo 7.3. : s[i:]    => vocales[2:]    resultado ==> {vocales[2:]}")   

    print(f"Ejemplo 7.4. : s[i::k]  => vocales[2::2]  resultado ==> {vocales[2::2]}")  

    print(f"Ejemplo 7.5. : s[:]     => vocales[:]     resultado ==> {vocales[:]}") 

    print(f"Ejemplo 7.6. : s[:j:k]  => vocales[:5:2]  resultado ==> {vocales[:5:2]}") 

    print(f"Ejemplo 7.7. : s[:j:k]  => vocales[:5:2]  resultado ==> {vocales[:5:2]}") 

    print(f"Ejemplo 7.8. : s[:j]    => vocales[:4]    resultado ==> {vocales[:4]}") 

    print(f"Ejemplo 7.9. : s[::k]   => vocales[::2]   resultado ==> {vocales[::2]}") 

    print(f"Ejemplo 7.10.: s[::k]   => vocales[::2]   resultado ==> {vocales[::2]}") 
if __name__ == "__main__":
    main()