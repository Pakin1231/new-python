#This program calculates the sum of a series of numbers the user enters.

max = 5 #The maximum number
# Initialize and accummulator variable
total = 0.0

#Explain what we are doing
print('This program calculates the sum of')
print(max, 'numbers you will enter.')

#Get the numbers and accmulate them.
for counter in range (max) :
    number = int (input('Enter a number: '))
    total = total + number

#Display the total of the numbers.
print('The total is', total)
