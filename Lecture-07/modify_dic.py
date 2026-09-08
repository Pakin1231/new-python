student = {"name": "Alice", "age": 25, "grade": "A"}

student["age"] = 26  # Update the age
student["major"] = "Computer Science"  # Add a new key-value pair
print(student)  # Output: {'name': 'Alice', 'age': 26, 'grade': 'A', 'major': 'Computer Science'}

remove_major = student.pop("major")  # Remove the 'major' key-value pair
print(remove_major)  # Output: Computer Science
print(student)  # Output: {'name': 'Alice', 'age': 26,