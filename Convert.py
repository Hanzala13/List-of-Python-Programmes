# Python program to convert Decimal to Binary
def decimal_to_binary(decimal_num):
    # Using bin() function
    binary_num = bin(decimal_num).replace("0b", "")
    return binary_num

# Input from the user
decimal_num = int(input("Enter a decimal number: "))

# Display the result
print(f"Binary representation of {decimal_num} is {decimal_to_binary(decimal_num)}")