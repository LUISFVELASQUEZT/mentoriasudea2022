#   Mentorias UdeA
#   Taller Introductorio a pandas
#   Mentor Luis F. Velásquez Tangarife
#   luisvelasquezt@protonmail.com
#   18 de mayo de 2022


import pandas as pd   # se importa el módulo pandas y se le asocia un alias pd para simplificar la referencia
import random

def sepBloques(texto):
    print("\n\n >>>>>>>>>>>>>>>", texto)

def calcImc(linea):
    imc = linea["Peso"] / pow(linea["Estatura"] ,2)  
    return imc

def pesoLibras(pesoKg):
    libras = pesoKg * 1000 / 454
    return libras


#carga  y vision inicial

csv_local_file = "./data/datos.csv"   #   ruta del archivo que se procesará
csv_output_file = "./data/salida.csv"

# usando el metodo read_csv de pandas se carg en el dataframe df el contenido del archivo
# el parámetro index_col="Cedula" indica que las filas se identificarán de manera única por el contenido de la columna "Cedula"

df = pd.read_csv(csv_local_file,index_col="Cedula")    

# Imprimir las primeras 5 filas para revisión visual

sepBloques("1. Los primeros registros son: >>>>>>>>\n\n")
print(df.head())
sepBloques("========================\n\n")
sepBloques("2. Los últimos registros son: >>>>>>>>\n\n")  
print(df.tail())   # Imprimir las últimas 5 filas para revisión visual
sepBloques("========================\n\n")
sepBloques("3. Las estadísticas básicas son: >>>>>>>>\n\n")
print(df.describe())  # Mostrar las estadísticas básicas de toda la población de datos en el dataframe
sepBloques("========================\n\n")
# Filtrar
sepBloques("4. El contenido completo es: >>>>>>>>\n\n")
print(df)
sepBloques("========================\n\n")
# Seleccionar
sepBloques("5. Selección de una sola columna: >>>>>>>>\n\n")
print(" ",df["Edad"])
sepBloques("6. Selección de tres columnas: >>>>>>>>\n\n")
print(df[["Edad","Sexo","Peso",]])
sepBloques("7. Selección de filas por rango de índices: >>>>>>>>\n\n")
print(df.iloc[0:4])
sepBloques("8. Selección de filas lista de valores de campo índice (Cedula), todas las columnas:")
print(df.loc[[221,1030,2140]])
sepBloques("9. Selección de filas con lista de valores de campo índice (Cedula), algunas columnas: >>>>>>>>\n\n")
print(df.loc[[221,1030,2140], ["Edad","Sexo","Peso"]])
sepBloques("10. Selección de filas condición (edad < 20 o peso < 60), todas las columnas: >>>>>>>>\n\n")
print(df[(df["Edad"] < 20.0) | (df["Peso"] < 60.0)])

df["IMC"] = df.apply(calcImc, axis=1)  # Calcula el IMC con función que recibe toda la linea de datos

df["Libras"] = df["Peso"].apply(pesoLibras)  # Calcula el Peso en libras con función que recibe solo un campo

sepBloques("11. Imprime los datos calculados  y otros datos del frame: >>>>>>>>\n\n")

print(df[["Edad","Nombres","Peso","Libras","Estatura","IMC"]])

sepBloques("12. Imprime los datos agrupados por sexo: >>>>>>>>\n\n")
print(df.groupby("Sexo").mean())  # agrupamiento por el campo sexo y calcula promedios

sepBloques("13. Filtrado por contenido de una cadena: >>>>>>>>\n\n")
print(df[(df["Nombres"].str.contains("fi"))])

df.to_csv(csv_output_file)
