#Example of the identity operator

#Two varibles pointing to the same list object
a = [1, 2, 3]
b = a

#Two variables pointing to different list objects with the same content
c = [1, 2, 3]
d = [1, 2, 3]

#Using the identity operator
print(a is b) #True, since a and b refer to the same object
print(a is c) #False, since a and c refer to different object
print(c is d) #False, since c and d refer to different object

#Using the equality operator for comparison 
print (a==c) #True, since the contents of a and c are equal
print (c==d) #True, since the contents of c and d are equal