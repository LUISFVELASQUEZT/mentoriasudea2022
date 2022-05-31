from modulefinder import IMPORT_NAME


import pandas as  pd

df  = pd.read_csv("all_conditions.csv")

print(f" Datos iniciales {df.head()}")

ages = df["age"]
print(f"Edades\n{ages} ")
print(f"Edades shape\n{ages.shape}")
      
age_sex = df[["age", "sex"]]
print(f"Age  sex\n{age_sex}")
print(f"Age  sex shape\n{age_sex.shape}")

print(f"Typeof\n{type(age_sex)}")

above_70 = df[df["age"] > 70] #& df[["sex"] == "f"]
print(f"Mayores 70\n{above_70}")

ages_71_80 = df[df["age"].isin([71, 80])]
print(f"De 71 u 80 ver is.in \n{ages_71_80}")


ages_71_80 = df[(df["age"] == 71) | (df["age"] == 80) ]
print(f"De 71 u 80 ver or\n{ages_71_80}")


#To create a new column, use the [] brackets with the new column name at the left side of the assignment.

df["age_times_11"] = df["age"] * 11.0

df1 = df[["age","age_times_11","sick"]]

print(f" edad incrementada\n{df1}")

#Estadisticas 
print("Media: " ,df1["age"].std())

#Create a new column by assigning the output to the DataFrame with a new column name in between the [].

df_renamed = df1.rename(
    columns={
        "sick": "Enfermo",
        "age": "Edad",
        "age_times_11": "Calculado",
    }
)

print(f" edad renombrado\n{df_renamed}")

#Operations are element-wise, no need to loop over rows.

#Use rename with a dictionary or function to rename row labels or column names.

print("Media: " ,df1["age"].mean())
print("Count: " ,df1["age"].count())
print("Descripcion: " ,df1["age"].describe())

print("Media: " ,df[["age","TT4"]].mean())

print("Media: \n" ,df[["age","TT4"]].describe())



print(" Agregados \n"
      ,df.agg(
      {
          "age":["min","max","count"],
          "TT4": ["count","std","mean"],
      }))

#titanic.agg(
#   {
#       "Age": ["min", "max", "median", "skew"],
#      "Fare": ["min", "max", "median", "mean"],
#   }
