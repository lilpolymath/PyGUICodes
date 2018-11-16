#Modules required
import seth

#details about courses and Units

courses = ['CSC212', 'CSC221', 'CSC231', 'CSC232', 'CSC233', 'CSC234', 'CSC241', 'CSC291', 'CSC292', 'GES103', 'GES201', 'MAT223', 'STA221', 'STA211']

weigth = [3,3,3,3,4,3,4,3,3,2,2,4,3,3]

scores = [seth.inputrange("Please enter your score for {} : " .format(courses[i]), 0,100) for i in range(len(courses))]

total = 0
for i in range(len(scores)):
    if scores[i] in range(45,50):
        points = 1
    elif scores[i] in range(50,60):
        points = 2
    elif scores[i] in range(60,70):
        points = 3
    elif scores[i] in range(70,101):
        points = 4
    else: points = 0

    points *= weigth[i]
    total += points

total_units = sum(weigth)
gpa = round((total/total_units),2)

print("Your GPA is {}" .format(gpa))

if 1.0 < gpa < 2.0:
    print("You are on THIRD CLASS.")
elif 2.0< gpa < 3.0:
    print("You are on a SECOND CLASS LOWER (2.2).")
elif 3.0< gpa <3.5:
    print("You are on a SECOND CLASS UPPER (2.1).")
elif gpa >= 3.5:
    print("You are on a FIRST CLASS.")
else:
    print("You have been widthdrawn from the University.")



first_year = float(input("Enter your GP in your first year: "))
first_year_units = float(input("Enter your total units for your first year: "))
