fruit = {"apple", "banana", "cherry"}

fruit.add("orange")
print(fruit) #output : {'apple', 'banana', 'cherry', 'orange'}
 
fruit.remove("banana")
print(fruit) #output : {'apple', 'cherry', 'orange'}

fruit.discard("grape")  # This will not raise an error if "grape" is not in the set
print(fruit) #output : {'apple', 'orange', 'cherry'} (no error is raised)

remove_item = fruit.pop()  # Removes and returns an arbitrary item from the set
print(remove_item)
print(fruit) #Output : {'cherry', 'orange'} (an arbitrary item is removed)

fruit.clear()  # Removes all items from the set
print(fruit)