# Student Database in a School
students = [
    {"id": "S001", "name": "John Doe", "course": "Math", "grade": 88},
    {"id": "S002", "name": "Jane Smith", "course": "Science", "grade": 92},
    {"id": "S003", "name": "Alice Johnson", "course": "History", "grade": 85}
]

for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Course: {student['course']}, Grade: {student['grade']}")
