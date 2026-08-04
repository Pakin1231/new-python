global_variable = "I'm outside the function"

def my_function():
    print(global_variable)

#
my_function()  # Output: I'm outside the function

#
print(global_variable)  # Output: I'm outside the function