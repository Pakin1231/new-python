# Getting user input and converting to int
Celsius = int(input("Please enter the temperature in Celsius: "))
Celsius = int(Celsius)  # Ensure Celsius is an integer

Fahrenheit = (Celsius * 9/5) + 32  # Convert Celsius to Fahrenheit
print("Temperature in Fahrenheit is:", format(Fahrenheit, ".2f"))