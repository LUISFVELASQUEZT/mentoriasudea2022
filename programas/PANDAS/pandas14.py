import pandas as pd

csv_local_fn = "./data/datos.csv"

df = pd.read_csv(csv_local_fn)  # dataFrame

print(df)

print(df.describe())
print(df[["Cedula","Nombres","Edad","Sexo","Peso",]])