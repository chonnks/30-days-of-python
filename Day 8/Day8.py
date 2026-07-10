#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
#To create a dictionary we use curly brackets, {} or the dict() built-in function.

#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name' : 'Goku', 
    'breed' : 'Labrador Retriever', 
    'legs' : 4,
    'age' : 13
}

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'Bruce',
    'last_name' : 'Reyes',
    'gender' : 'Male',
    'age' : 22,
    'martial status' : 'single',
    'skills' : ['soccer', 'drawing', 'gaming'],
    'city' : 'Waldorf',
    'address' : '123 Street Road'
}

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(type(student['skills']))

#Modify the skills values by adding one or two skills
student['skills'].append('pool')
student['skills'].append('fashion')

print(student['skills'])

#Get the dictionary keys as a list
keys_list = student.keys()
print(keys_list)

#Get the dictionary values as a list
values_list = student.values()
print(values_list)

#Change the dictionary to a list of tuples using items() method
student_to_tuple = student.items()
print(student_to_tuple)

#Delete one of the items in the dictionary
del(student['city'])
print(student)

#Delete one of the dictionaries
del(student)


