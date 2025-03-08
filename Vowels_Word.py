def count_names_with_vowels(names):
    vowels = {'A', 'E', 'I', 'O', 'U'}  # Set for faster lookup
    count = sum(name[0].upper() in vowels for name in names)
    return count

# Example usage
names_list = ["Alice", "Eve", "Oscar", "Uma", "Bob", "Charlie"]
result = count_names_with_vowels(names_list)
print(f"Number of names starting with a vowel: {result}")
