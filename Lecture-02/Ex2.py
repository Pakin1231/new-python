# Getting user input and converting to int
weight = int(input("Please enter your weight: "))
weight = int(weight)  # Ensure weight is an integer

# Getting user input and converting to float
height = float(input("Please enter your height: "))
height = float(height)  # Ensure height is a float

bmi = weight / (height * height)  # Calculate BMI
print("Your BMI is:", bmi)