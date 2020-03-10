# Check to see if requirements for honor roll are met
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= 85 and lowest_grade >= 70:
    honor_roll = True
else:
    honor_roll = False

# Somewhere later in your code if you need to check if students is
# on honor roll, all I need to do is check the boolean variable
# I set earlier in the code
# if honor_roll is same as saying if honor_roll = True - but is using accepted syntax
if honor_roll:
    print('You made the honor roll!')