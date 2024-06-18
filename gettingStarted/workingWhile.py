# while function project

total = 0
numGrades = 0
studentName = input("Enter student name: ")
totGrades = int(input("Enter number of grades to process: "))
while numGrades < totGrades:
    grade = int(input("Enter assignment grade: "))
    numGrades = totGrades + 1
    total = total + grade
average = total / totGrades

print(studentName + " has earned an average of: " + str(average))
