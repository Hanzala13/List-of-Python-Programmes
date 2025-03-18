def find_smallest_number(numbers):
    if not numbers:
        return "List is empty"
    
    smallest = numbers[0]  # Assume first element is smallest
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

# Example usage
numbers = [23, 1, 45, 78, -5, 0, 34]
print(f"The smallest number is: {find_smallest_number(numbers)}")
