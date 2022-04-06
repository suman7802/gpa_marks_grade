print("Enter Your GPA \"0-4\"")
GPA = float(input())
grade = ""
print("You Enter Your GPA", GPA)
if 3.60 < GPA < 4.01:
    grade = 'A+'
elif 3.20 < GPA < 3.61:
    grade = 'A'
elif 2.80 < GPA < 3.21:
    grade = 'B+'
elif 2.40 < GPA < 2.81:
    grade = 'B'
elif 2.00 < GPA < 2.41:
    grade = 'C+'
elif 1.60 < GPA < 2.01:
    grade = 'C'
elif 1.20 < GPA < 1.61:
    grade = 'D+'
elif 0.80 < GPA < 1.21:
    grade = 'D'
elif 0.00 < GPA < 0.81:
    grade = 'E'
else:
    grade = 'null'
print("Your Grade Is", grade)
print("Your MARKS Is", GPA * 25)
if GPA < 1.60:
    print("You can try for NEB re-exam on the particular subject")
