setA = {1, 2, 3, 4}
setB = set([8, 9, 10])

setA.add(5)
setB.update([6, 7])
Uset = setA | setB
print(Uset)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(len(Uset))  # Output: 10

setB.update('ABCD')
setA.update([6,7,8])
print(setB)  # Output: {6, 7, 8, 9, 10, 'A', 'B', 'C', 'D'}

print(setA.intersection(setB))  # Output: {6, 7, 8}
print(setA ^ setB)  # Output: {1, 2, 3, 4, 5, 'A', 'B', 'C', 'D'}

setB.remove('8')
setB.discard('10')
print(setB)  # Output: {6, 7, 9, 'A', 'B', 'C', 'D'}
print(setA.clear())  # Output: None
for val in Uset:
    print(val)  # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (order may vary)