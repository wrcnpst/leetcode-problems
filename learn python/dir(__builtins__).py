student_grades = [9.1, 8.8, 7.5]

# dir(__builtins__)
# we gonna find mean in the list

sum_grades = sum(student_grades)
count_std = len(student_grades)
max_grade = max(student_grades)

mean_grades = sum_grades / count_std

print(max_grade)


# dir(dict)
student_grades_dict = {'Marry': 9.1, 'Sofia': 8.8, 'Jim': 7.5}
sum(student_grades_dict.values())
