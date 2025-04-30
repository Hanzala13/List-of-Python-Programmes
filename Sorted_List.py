def is_sorted_ascending(lst):
    return lst == sorted(lst)

# Example usage:
numbers = [1, 2, 3, 4, 5]
print(is_sorted_ascending(numbers))  # Output: True

numbers2 = [5, 3, 2, 1]
print(is_sorted_ascending(numbers2))  # Output: False
