def count_names_starting_with_vowel(names):
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for name in names:
        if name and name[0].lower() in vowels:
            count += 1
    return count

# Example usage
name_list = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Charlie", "Ian"]
result = count_names_starting_with_vowel(name_list)
print(f"Number of names starting with a vowel: {result}")
