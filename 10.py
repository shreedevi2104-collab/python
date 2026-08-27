# Student Grade Calculator using python program language 

name = input("Enter your name: ")

marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)
