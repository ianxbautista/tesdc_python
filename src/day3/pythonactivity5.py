name = input(f'Enter your name: ')
PhysicsGrade = float(input(f'Enter your Grade in Physics: '))
AlgebraGrade = float(input(f'Enter your Grade in Algebra: '))
ProgramGrade = float(input(f'Enter your Grade in Programming: '))
AverageGrade = (PhysicsGrade + AlgebraGrade + ProgramGrade)/3
GradeStatus = ""
if AverageGrade < 78:
    GradeStatus = "Failure"
elif 78 <= AverageGrade <= 82:
    GradeStatus = "Fair"
elif 83 <= AverageGrade <= 88:
    GradeStatus = "Average Student"
elif 89 <= AverageGrade <= 94:
    GradeStatus = "Dean's Lister"
elif 95 <= AverageGrade <= 100:
    GradeStatus = "President's List"
else:
    GradeStatus = "Invalid Grade"

print(f'{name} Average Grade: '"{:.2f}".format(AverageGrade))
print(f'{GradeStatus}')