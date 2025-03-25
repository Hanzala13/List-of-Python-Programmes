def rotate_array(arr, steps):
    n = len(arr)
    steps = steps % n  # Handle cases where steps > n

    # Rotate array using slicing
    rotated_arr = arr[-steps:] + arr[:-steps]
    return rotated_arr

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    steps = int(input("Enter number of steps to rotate: "))
    print(f"Original array: {arr}")
    rotated_arr = rotate_array(arr, steps)
    print(f"Rotated array: {rotated_arr}")
