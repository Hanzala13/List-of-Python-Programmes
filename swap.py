a = [67, 74 ,976 , 24 , 53]
b = a[1]
a[1] = a[4]
a[4] = b
print(a)
print(b)