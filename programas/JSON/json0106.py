#importing the json module
# ejemplo tomado de https://www.codespeedy.com/python-json-encoder-and-decoder/
import json

#giving a json data string
jsn_str = '{"name": "Sourav", "age": 20, "student": true, "roll no": 45, "subjects": ["Python", "Java"]}'

#decoding the JSON format into Python dictionary using loads() method
decoded_dict = json.loads(jsn_str)

#printing the Python dictionary
print(decoded_dict)

#checking the type of decoded_dict
print("Type of decoded_dict", type(decoded_dict))