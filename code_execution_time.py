import datetime
# if you add from datetime import datetime, then in your function you only have to
# call datetime once and not refer to the datetime within the datetime libarry

# print timestamps to see how long sections of code take to run
# call the function instead of repeat copy/pasting code

# Function to print current date and time

# when you put parameters in function you have to put in values for it
# by adding task_name into def print_time() function you need to add a 
# text you want passed each time it runs when the function it called below

def print_time(task_name):
    print(task_name)
    print(datetime.datetime.now())
    print()

first_name = 'Susan'
print_time('printed first name')

for x in range (0,10):
    print(x)
print_time('completed for loop')