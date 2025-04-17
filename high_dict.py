# List of dictionaries
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]

# Find the dictionary with the highest value for the key 'score'
highest_score_student = max(students, key=lambda x: x["score"])

# Print the result
print("Student with the highest score:")
print(highest_score_student)
