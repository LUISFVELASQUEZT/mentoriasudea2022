#importing json module
# EJEMPLO tomado de  https://www.codespeedy.com/python-json-encoder-and-decoder/
import json
test = {
  "name": "Sourav",
  "age": 20,
  "student": True,
  "roll no": 45,
  "subjects": ("Python","Java")
}
#sorting the result in ascending order by keys:
#using indent parameter to change the format of the code
sorted_str = json.dumps(test, indent = 5,sort_keys=True)
print(sorted_str)