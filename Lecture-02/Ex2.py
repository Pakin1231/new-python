# Getting user input and converting to int
weight = int(input("Please enter your weight in kilograms: "))
weight = int(weight)  # Ensure weight is an integer

# Getting user input and converting to float
height = float(input("Please enter your height in meters: "))
height = float(height)  # Ensure height is a float

bmi = weight / (height ** 2)  # Calculate BMI
print("Your BMI is:", (bmi, ".2f"))