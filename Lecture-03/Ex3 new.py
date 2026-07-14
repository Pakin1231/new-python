work_hour = int(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the number of hourly rate: "))
#if work_hour > 40:
if work_hour <= 40:
    pay = work_hour * hourly_rate
else:
    pay = (work_hour - 40) * hourly_rate * 1.5 + (40 * hourly_rate)
print("Total pay for the week: $", format(pay,".2f"))