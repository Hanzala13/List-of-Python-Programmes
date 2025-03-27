import math

def find_lcm(a, b):
    # Using the formula: LCM(a, b) = |a * b| / GCD(a, b)
    return abs(a * b) // math.gcd(a, b)

# Taking user input
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Finding and displaying the LCM
    result = find_lcm(num1, num2)
    print(f"The LCM of {num1} and {num2} is {result}")

except ValueError:
    print("Please enter valid integers.")
