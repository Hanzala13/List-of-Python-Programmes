def cube_sum(n):
    # Using the formula for cube sum of first n natural numbers: (n(n+1)/2)^2
    return (n * (n + 1) // 2) ** 2

# Input from the user
try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = cube_sum(n)
        print(f"The cube sum of the first {n} natural numbers is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
