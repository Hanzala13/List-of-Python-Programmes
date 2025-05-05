A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A.union(B)
intersection = A.intersection(B)
difference_A_B = A.difference(B)
difference_B_A = B.difference(A)

print("Union:", union)
print("Intersection:", intersection)
print("A - B:", difference_A_B)
print("B - A:", difference_B_A)
