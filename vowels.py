def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Example usage
string = "Hello, World!"
print("Number of vowels:", count_vowels(string))  # Output: 3
