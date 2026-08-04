def is_armstrong(number):
    # Convert the number to a string to iterate over its digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the calculated sum is equal to the original number
    return armstrong_sum == number

# Example usage
print(is_armstrong(153))  # Output: True (153 = 1^3 + 5^3 + 3^3)
print(is_armstrong(9474))  # Output: True (9474 = 9^4 + 4^4 + 7^4 + 4^4)
print(is_armstrong(123))  # Output: False (123 != 1^3 + 2^3 + 3^3)