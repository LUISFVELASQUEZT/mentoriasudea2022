import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5) , index=["Valor 1", "Valor 2", "Valor 3", "Valor 4", "Valor5"]) 

print("Serie")
print(s)

d = {"b": 1, "a": 0, "c": 2}  

print("Serie bac")
pd.Series(d) 

print(d) 
e={"c": 2.0, "a": 0.0, "b": 1.0}
     
pd.Series(e, index=["b", "c", "d", "a"])
print("Serie bcda")
print(e) 

# Escalares
print("Escalares")
print(pd.Series(5.0, index=["a", "b", "c", "d", "e"]))

# Slicing


se = pd.Series(np.random.randn(5) , index=["Valor 1", "Valor 2", "Valor 3", "Valor 4", "Valor 5"]) 

print("Serie slicing")
print(f"Serie completa\n{se}")
print(f"Elemento 0 {se[0]}")
print(f"Elementos 0,1 y 2 \n{se[:3]}")
print(f"Condicional sobre media: {se.median()}\n{se[se > se.median()]}")

print(f"Elementos 4,3,1\n{se[[4,3,1]]}")


 



