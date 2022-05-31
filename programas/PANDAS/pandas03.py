import pandas as pd
import random

#csv_url = "https://raw.githubusercotent.com/datasets/gdp/master/data/gdp.csv"

#carga  y vision inicial
csv_local_file = "all_conditions.csv"
#df = pd.read_csv(csv_local_file)
df = pd.read_csv(csv_local_file,index_col="patient_id")
#print(df.head())
#print(df.tail())
#print(df.describe())
# Filtrar

#print(df)

#df_limpio = df.dropna()
#print(df)
#print(df_limpio)

# Seleccionar

#print(df["age"])

#print(df[["age","sex","target_hyper"]])

#print(df.iloc[0:12])

#print(df.loc[[806,3652,3331]])

#print(df.loc[[806,3652,3331], ["age","sex","target_sick"]])

#print(df[(df["age"] > 70.0) | (df["age"] < 20.0)])

# print(df[["age","sex","target_sick"]])



#print(df[(df["target_hyper"].str.contains("hyper")), ["age","sex","target_sick"]])

def calcPrioridad(edad):
   prioridad = edad * random.randint(3,5)
   return prioridad

def sumaIndicadores(linea):
    resultado = linea["TSH"] + linea["T3"] + linea["TT4"]
    return resultado

df["resultado" ] = df.apply(sumaIndicadores, axis=1)


df["prioridad"] = df["age"].apply(calcPrioridad)

print(df[["age","prioridad","resultado"]])





#print(df.groupby("age").mean())