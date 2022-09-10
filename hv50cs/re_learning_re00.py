import re

email = input("Your email pls. :")

#if re.search(r"^[a-zA-Z0-9_.]+@[^@][^ ]+\.(gov|com|edu)$",email):
#if re.search(r"^\w+@\w+\.(gov|com|edu)$",email):
#if re.search(r"^(\w+\.)?\w+@(\w+\.)?\w+\.(gov|com|edu)$",email):
if re.search(r"^(\w+\.)?\w+@(\w+\.)?\w+\.(gov|com|edu)$",email):   
    print("Valid")
else:
    print("Invalid")


    