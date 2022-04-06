print("Enter Your marks 0 - 100")
marks = int(input())
grade = ""
print("You Enter Your MarkS", marks)
if 90 < marks == 100:
    grade = 'A+'
elif 80 < marks < 91:
    grade = 'A'
elif 70 < marks < 81:
    grade = 'B+'
elif 60 < marks < 71:
    grade = 'B'
elif 50 < marks < 61:
    grade = 'C+'
elif 40 < marks < 51:
    grade = 'C'
elif 30 < marks < 41:
    grade = 'D+'
elif 20 < marks < 31:
    grade = 'D'
elif 0 < marks < 21:
    grade = 'E'
else:
    grade = 'null'
print("Your Grade Is", grade)
print("Your GPA Is", marks / 25)
if marks < 40:
    print("You can try for NEB re-exam on the particular subject")
