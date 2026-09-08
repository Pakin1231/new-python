set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

set1 &= set2  # Intersection assignment
print("After intersection assignment, set1:", set1)  # Output: {4, 5}

#Resetting set1 to original values
set1 = {1, 2, 3, 4, 5}

set1 -= set2  # Difference assignment
print("After difference assignment, set1:", set1)  # Output: {1, 2, 3}

set1 = {1, 2, 3, 4, 5}

set1 ^= set2  # Symmetric difference assignment
print("After symmetric difference assignment, set1:", set1)  # Output: {1, 2, 3, 6, 7}
