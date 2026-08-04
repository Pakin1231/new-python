def format_strings(*args):
    """
    This function takes multiple string arguments, concatenates them,
    and returns the result in uppercase.
    
    :param args: Variable length string arguments
    :return: Concatenated uppercase string
    """
    # Concatenate all strings and convert to uppercase
    return ''.join(args).upper()    

#Example usage
result = format_strings("Hello", "World", "this", "is", "a", "test")
print(result)  # Output: "HELLOWORLDTHISISATEST"

result = format_strings("Python", "is", "fun")
print(result)  # Output: "PYTHONISFUN"

result = format_strings("Concatenate", "these", "strings","please")
print(result)  # Output: "CONCATENATETHESESTRINGSPLEASE"