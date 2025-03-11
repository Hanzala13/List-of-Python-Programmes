def calculate_sum_and_average(numbers):
    total = sum(numbers)  # Calculates the sum
    average = total / len(numbers) if numbers else 0  # Calculates the average
    return total, average

# Example usage
numbers = [10, 20, 30, 40, 50]
total, average = calculate_sum_and_average(numbers)
print(f"Sum: {total}")
print(f"Average: {average}")
