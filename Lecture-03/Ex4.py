Add = 1
Subtract = 2
Mutiply = 3
Divide = 4

choice = float(input("Enter the number of Operation Add = 1 Subtract = 2,Mutiply = 3,Divide = 4 : "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print(f"{num1} + {num2} = {num1 + num2}")

elif choice == 2:
    print(f"{num1} - {num2} = {num1 - num2}")

elif choice == 3:
    print(f"{num1} * {num2} = {num1 * num2}")

elif choice == 4:
    print(f"{num1} / {num2} = {num1 / num2}")