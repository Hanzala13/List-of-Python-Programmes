def is_disarium(num):
    # Convert number to string to iterate its digits
    digits = str(num)
    # Calculate the sum of digits raised to their respective positions
    total = sum(int(digit) ** (index + 1) for index, digit in enumerate(digits))
    # Check if the sum matches the original number
    return total == num

# Input from the user
try:
    number = int(input("Enter a number: "))
    if is_disarium(number):
        print(f"{number} is a Disarium Number.")
    else:
        print(f"{number} is not a Disarium Number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")