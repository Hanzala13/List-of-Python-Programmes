def is_monotonic(arr):
    # Check if the array is either non-increasing or non-decreasing
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or \
           all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

# Example usage
if __name__ == "__main__":
    array1 = [1, 2, 2, 3, 4]    # Monotonic Increasing
    array2 = [5, 4, 4, 3, 2]    # Monotonic Decreasing
    array3 = [1, 3, 2, 4, 5]    # Not Monotonic

    print(f"Array 1 is monotonic: {is_monotonic(array1)}")
    print(f"Array 2 is monotonic: {is_monotonic(array2)}")
    print(f"Array 3 is monotonic: {is_monotonic(array3)}")
