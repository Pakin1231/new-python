payrate = 20
num = float(input("Enter the number of hours worked"))
if num > 40:
	pay = payrate * 40 + (num - 40) * payrate * 1.5
else:
	pay = payrate * num

print("The gross pay:", pay)
