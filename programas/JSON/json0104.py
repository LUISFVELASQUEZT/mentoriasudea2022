#importing json module
# ejemplo tomado de https://www.codespeedy.com/python-json-encoder-and-decoder/
import json
test = {
  "name": "Sourav",
  "age": 20,
  "student": True,
  "roll no": 45,
  "subjects": ("Python","Java")
}
#we are creating a new test_json.json file with the write mode using file i/o operation 
with open('test_json.json', "w") as file_write:
#writing json data into the file
    json.dump(test, file_write)