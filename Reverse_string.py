def reverse_string(s):
    return s[::-1]

# Taking user input
string = input("Enter a string to reverse: ")
reversed_string = reverse_string(string)
print(f"Reversed string: {reversed_string}")
