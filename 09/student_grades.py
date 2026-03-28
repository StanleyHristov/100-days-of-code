student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = student_scores.copy()

for student, score in student_scores.items():
    if score >90:
        student_grades[student] = "A"
    elif score>80:
        student_grades[student] ="B"
    elif score>70:
        student_grades[student] = "C"
    else:
        student_grades[student] = "F"
print(student_grades)