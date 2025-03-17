def find_largest_number(arr):
    if not arr:
        return "Array is empty"
    
    largest = arr[0]  # Assume the first element is the largest
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Example usage
numbers = [10, 45, 23, 89, 12, 78, 56]
print(f"The largest number in the array is: {find_largest_number(numbers)}")
