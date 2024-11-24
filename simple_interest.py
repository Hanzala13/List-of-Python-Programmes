def simple_interest(p, t , r):
    print('The principal is:', p)
    print('The time period is:', t)
    print('The rate is:', r)

    SI = (p * t * r)/100

    print("The simple interest is :", SI)

p = int(input("Enter the principal amount : "))
t = int(input("Enter the time period : "))
r = int(input("Enter the rate of interest : "))
simple_interest(p, t, r)