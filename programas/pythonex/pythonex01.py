name = input(" Pls enter your name:")

age = int(input("Your age: "))
comment = ""
if age < 20:
    comment =" Menor de edad."
else:
    comment = "Mayor de edad"
print(f"Hello {name.upper()}. You are {age} years old! You are {comment}")