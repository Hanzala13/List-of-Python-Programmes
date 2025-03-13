def union_lists(list1, list2):
    """
    Returns the union of two lists (all unique elements).
    """
    # Using set to ensure uniqueness
    return list(set(list1) | set(list2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8, 5, 9]

result = union_lists(list1, list2)
print("Union of the two lists:", result)
