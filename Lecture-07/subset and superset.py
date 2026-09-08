set_a = {1, 2, 3, 4}
set_b = {2, 3}
set_c = {1, 2, 3, 4}
set_d = {1, 2, 3, 4, 5}

#Superset and subset
print("is set_a a superset of set_b?", set_a >= set_b)  # Output: True
print("is set_b a subset of set_a?", set_b <= set_a)  # Output: True

#Proper superset and subset
print("is set_a a proper superset of set_b?", set_a > set_b)  # Output: True
print("is set_b a proper subset of set_a?", set_b < set_a)  # Output: True

#Equal Sets
print("is set_a equal to set_c?", set_a == set_c)  # Output: True

#Relation but not equal (one is subset but not equal)
print("is set_b a superset of set_d and not equal?", set_b <= set_d and set_b != set_d)  # Output: True