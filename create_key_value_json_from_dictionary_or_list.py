import json
# Note: Use print statements all over the place to help you debug if you run into issues
# Use JSON linter online for easier view of lots of JSON code

# Create a dictionary object
person_dict = {'first': 'Christopher', 'last':'Harrison'}
# Add additional key pairs as needed to dictionary
person_dict['City']='Seattle'

# Convert dictionairy to JSON object
person_json = json.dumps(person_dict)
print(person_json)

# If you need subkeys and subvalues as well 
# (essentially creating a dictionary within a dictionary)
person_dict = {'first': 'Christopher', 'last': 'Harrison'}

# Create staff dictionary which assigns a person to a role
staff_dict = {}
staff_dict['Program Manager']=person_dict

# Convert dictionary to JSON object
staff_json = json.dumps(staff_dict)

# Print JSON object
print(staff_json)

# Add lists to the dictionary to create JSON 

# Create a list object of programming languages
languages_list = ['CSharp', 'Python', 'JavaScript']

# Add list to dictionary
person_dict['languages'] = languages_list

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)
print(person_json)