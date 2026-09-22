import json

data = {"name": "Alice", "age": 25}
json_str = json. dumps (data)
print (json_str) # Output: JSON string

parsed_data = json. loads (json_str)
print (parsed_data) # Output: Python dictionary
print (parsed_data ["name"]) # Output: Alice
print (parsed_data ["age"]) # Output: 25