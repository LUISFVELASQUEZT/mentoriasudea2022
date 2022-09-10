import re

my_ip_address = "11.122.133.144"

#hallado = re.search(r'^([0-9]{1-3}\.){3}[0-9]{3}$', my_ip_address) 

hallado = re.search(r'^([0-9]{1-3}[.]){3}[0-9]{3}$', my_ip_address) 



if hallado:
    print("Hallado")
else:
    print("No hallado")

str = 'purple alice-b@google.com monkey dishwasher'

#match = re.search(r'[\w.-]+@[\w.-]+', str)
match = re.search(r'\w+@\w+', str)


if match:
   print(match.group())  ## 'alice-b@google.com'


match = re.search(r'[\w.-]+@[\w.-]+', str)

if match:
    print(match.group())  ## 'alice-b@google.com'

str = 'purple aliceb@google.com monkey dishwasher'

match = re.search(r'[\w.-]+@[\w.-]+', str)

if match:
    print(match.group())  ## 'alice-b@google.com'

