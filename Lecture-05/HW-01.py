def format_strings(*args, sep=''):
    """
    This function takes multiple string arguments, concatenates them using an
    optional separator, and returns the result in uppercase.
    
    :param args: Variable length string arguments
    :param sep: Optional separator inserted between provided strings
    :return: Concatenated uppercase string
    """
    return sep.join(args).upper()

result = format_strings("Hello", "World", "this", "is", "a", "test")
print(result)

result = format_strings("Python", "is", "fun")
print(result)

#(ส่ง sep='-' เข้าไป)
result = format_strings("Hello", "World", sep="-")
print(result)