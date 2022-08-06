student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
grade_to_scores = {
  "Outstanding": lambda x: x > 90,
  "Exceeds Expectations" : lambda x: x > 80,
  "Acceptable" : lambda x: x > 70,
  "Fail" : lambda x: x <= 70
}
for student in student_scores:
  for grade in grade_to_scores:
    if grade_to_scores[grade](student_scores[student]):
      student_grades[student] = grade
      break


# 🚨 Don't change the code below 👇
print(student_grades)





