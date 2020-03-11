# if you have a list of items and want to print them out, this is perfect
# extra print statements are just for adding extra line for readability
people = ['Christopher', 'Susan']
print()
for name in people:
    print (name)
print()

# range automatically creates a list of numbers for us
# 0 is start and 2 is number of items to get
for index in range (0, 2):
    print(index)
print()

# while loop
# we specifiy the condition then it stays in the while loop
# at some point this needs to test as false or will be stuck forever
names = ['Christopher', 'Susan']
index = 0
while index < len(people):
    print(people[index])
    index = index + 1
print()    

  