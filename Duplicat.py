def remove_duplicates(input_string):
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

# Example usage:
text = "programming"
print(remove_duplicates(text))  # Output: "progamin"
