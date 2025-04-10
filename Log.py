import math

def calculate_natural_log():
    try:
        number = float(input("Enter a positive number to calculate its natural logarithm: "))
        if number <= 0:
            print("Error: Natural logarithm is only defined for positive numbers.")
        else:
            result = math.log(number)
            print(f"The natural logarithm of {number} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the function
calculate_natural_log()
