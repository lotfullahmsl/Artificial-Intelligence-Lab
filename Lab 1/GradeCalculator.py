print("=== Grade Calculator ===")
print()


num_subjects = int(input("Enter number of subjects: "))

total_marks = 0


for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks for subject {i} (out of 100): "))
    total_marks += marks


average = total_marks / num_subjects


if average >= 85:
    grade = 'A'
elif average >= 80:
    grade = 'A-'
elif average >= 75:
    grade = 'B+'
elif average >= 70:
    grade = 'B'
elif average >= 65:
    grade = 'B-'
elif average >= 60:
    grade = 'C+'
elif average >= 55:
    grade = 'C'
elif average >= 50:
    grade = 'C-'
else:
    grade = 'F'


print()
print("=== Results ===")
print(f"Total Marks: {total_marks}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
