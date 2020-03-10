# A student makes honor roll if their average is >=85
# and their lwest grade is not below 70
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

# could do the float conversion on its own line if you needed for simplicity
# lowest_grade = float(lowest_grade)
# could use .85 or .70
if gpa >= 85:
    if lowest_grade >= 70:
        print('You made the honor roll')