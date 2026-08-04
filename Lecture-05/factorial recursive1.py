def factorial(n):
    if n == 0 or n == 1:
        return 1 # Base case
    else:
        return n * factorial(n - 1) # Recursive case
    
# Example usage
print(factorial(5))  # Output: 120