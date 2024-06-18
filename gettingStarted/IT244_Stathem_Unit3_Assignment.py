total = 0
numGrades = 0
studentName = input("Enter student name: ")
sumGrades = int(input("Enter number of grades to process: "))
while numGrades < sumGrades:
    grade = int(input("Enter assignment grade: "))
    numGrades = numGrades + 1
    total = total + grade
average = total / sumGrades

print(studentName + " has earned an average of: " + str(average))