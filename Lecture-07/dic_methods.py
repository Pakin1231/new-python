student = {"name": "Alice", "age": 26, "major": "Computer Science"}

print(student.key())  # Output: dict_keys(['name', 'age', 'grade', 'major'])
print(student.values())  # Output: dict_values(['Alice', 26, 'A', 'Computer Science'])
print(student.items())  # Output: dict_items([('name', 'Alice'), ('age', 26), ('grade', 'A'), ('major', 'Computer Science')])

print(student.get("name"))  # Output: Alice
print(student.get("grade", "Not found"))  # Output: Not found

major = student.pop("major")  # Remove the 'major' key-value pair
print(major)  # Output: Computer Science
print(student)  # Output: {'name': 'Alice', 'age': 26, 'grade': 'A'}

last_item = student.popitem()  # Remove the last inserted key-value pair
print(last_item)  # Output: ('grade', 'A')
print(student)  # Output: {'name': 'Alice', 'age': 26}

student.clear()  # Clear all key-value pairs from the dictionary
print(student)  # Output: {}