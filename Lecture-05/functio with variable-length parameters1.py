def display_info(name, age, **kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# city: New York
# age: 30
