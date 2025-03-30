# Original list
original_list = [1, 2, 3, 4, 5]

# Method 1: Using slicing
cloned_list1 = original_list[:]

# Method 2: Using list() constructor
cloned_list2 = list(original_list)

# Method 3: Using copy() method
cloned_list3 = original_list.copy()

# Method 4: Using deepcopy() from the copy module (useful for nested lists)
import copy
cloned_list4 = copy.deepcopy(original_list)

# Display the results
print("Original List:", original_list)
print("Cloned List (Slicing):", cloned_list1)
print("Cloned List (list() constructor):", cloned_list2)
print("Cloned List (copy() method):", cloned_list3)
print("Cloned List (deepcopy method):", cloned_list4)
