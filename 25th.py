# Student Grade Calculator using python programming language 

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

print("Student Name:", name)
print("Marks:", marks)

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Grade: Fail")
