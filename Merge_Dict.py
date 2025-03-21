# Python program to merge two dictionaries
def merge_dicts(dict1, dict2):
    # Using the unpacking operator (**) for merging
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

# Merging dictionaries
result = merge_dicts(dict1, dict2)
print("Merged Dictionary:", result)
