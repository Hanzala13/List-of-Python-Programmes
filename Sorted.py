def is_sorted_ascending(elements):
    return elements == sorted(elements)

# Sample list
given_list = [1, 2,6, 4, 5]

# Check if sorted
if is_sorted_ascending(given_list):
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.")
