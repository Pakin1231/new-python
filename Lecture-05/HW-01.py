def format_strings(*args, sep=''):
    """
    This function takes multiple string arguments, concatenates them using an
    optional separator, and returns the result in uppercase.
    
    :param args: Variable length string arguments
    :param sep: Optional separator inserted between provided strings
    :return: Concatenated uppercase string
    """
    return sep.join(args).upper()

#Example usage
result = format_strings("Hello", "World", "this", "is", "a", "test")
print(result)  # Output: "HELLOWORLDTHISISATEST"

result = format_strings("Python", "is", "fun")
print(result)  # Output: "PYTHONISFUN"

result = format_strings("Concatenate", "these", "strings","please")
print(result)  # Output: "CONCATENATETHESESTRINGSPLEASE"