attendance_week = [
    ["Alice", "Bob", "Charlie","David"],
    ["Alice", "Charlie", "David"],
    ["Alice", "Bob", "David"],
    ["Alice", "David", "Eve"],
    ["Bob", "Charlie", "David",]
]

attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)  # Output: [{'Alice', 'Bob', 'Charlie', 'David'}, {'Alice', 'Charlie', 'David'}, {'Alice', 'Bob', 'David'}, {'Alice', 'David', 'Eve'}, {'Bob', 'Charlie', 'David'}]

present_every_day = set.intersection(*attendance_sets)
print("Present every day:", present_every_day)  # Output: {'David'}

all_students = set.union(*attendance_sets)
absent_at_least_one_day = all_students - present_every_day
print("Absent at least one day:", absent_at_least_one_day)  # Output: {'Alice', 'Bob', 'Charlie', 'Eve'}

first_day_present = attendance_sets[0]
last_day_present = attendance_sets[-1]
first_day_but_not_last = (first_day_present - last_day_present)
print("Present on first day but not on the last day:", first_day_but_not_last)  # Output: {'Alice'}

unique_students_count = len(all_students)
print("Total unique students:", unique_students_count)  # Output: 5

