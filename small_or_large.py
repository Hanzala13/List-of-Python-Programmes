def find_min_max(lst):
    if not lst:
        return None, None  # Handle empty list case

    # Using built-in functions
    smallest = min(lst)
    largest = max(lst)

    return smallest, largest

# Example usage
if __name__ == "__main__":
    numbers = [34, 12, 78, 56, 89, 23, 67, 45]
    smallest, largest = find_min_max(numbers)

    print(f"Smallest element: {smallest}")
    print(f"Largest element: {largest}")
