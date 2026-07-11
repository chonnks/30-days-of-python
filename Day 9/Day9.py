# Conditionals
# By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two ways:

# Conditional execution: a block of one or more statements will be executed if a certain expression is true
# Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. 


#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:

# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

age = int(input('Enter your age: '))

if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18 - age} more years to learn to drive')


#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
#You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.

your_age = 25
my_age = int(input('Enter my age: '))

if your_age > my_age and abs(your_age - my_age) == 1:
    print(f'I am {abs(your_age - my_age)} year older than you')
elif your_age < my_age and abs(your_age - my_age) == 1:
    print(f'You are {abs(your_age - my_age)} year older than me')
elif your_age > my_age and abs(your_age - my_age) > 1:
    print(f'I am {abs(your_age - my_age)} years older than you')
elif your_age < my_age and abs(your_age - my_age) > 1:
    print(f'You are {abs(your_age - my_age)} years older than me')
else:
    print('We are the same age')


#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

first_input = int(input('Enter number one: '))
second_input = int(input('Enter number two: '))

if first_input > second_input:
    print(f'{first_input} is greater than {second_input}')
elif second_input > first_input:
    print(f'{second_input} is greater than {first_input}')
else:
    print(f'The numbers are both equal')


##Exercises Level 2##
#Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```

grade = int(input('Enter your grade score: '))

if grade >= 90:
    print('Your grade is an A')
elif grade >= 80 and grade < 90:
    print('Your grade is a B')
elif grade >= 70 and grade < 80:
    print('Your grade is a C')
elif grade >= 60 and grade < 70:
    print('Your grade is a D')
else:
    print('You grade is an F')

#Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring. 
# June, July or August, the season is Summer

month = input('Enter the month: ')

if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('The season is Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('The season is Spring')
else:
    print('The season is Summer')



# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input('Enter your fruit: ')
print(new_fruit)

if new_fruit not in fruits: #use not in to find if it isn't in the list
    fruits.append(new_fruit)
    print(fruits)
else:
    print('That fruit already exists in the list')


###Exercise Level 3###
# Here we have a person dictionary. Feel free to modify it!

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][2])

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and 'Python' in person['skills']:
    print('This person has the Python skill')
else:
    print('This person does not have the Python skill')

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if 'Node' in person ['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills'] and 'JavaScript' in person ['skills'] and 'React' in person['skills']:
    print('He is a full stack developer')
elif 'Node' in person ['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a back end developer')
elif 'JavaScript' in person ['skills'] and 'React' in person['skills']:
    print('He is a front end developer')
else: 
    print('unknown title')


#* If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

if person['is_married'] == True and person['country'] == 'Finland':
    print(f'{person["first_name"]} lives in {person["country"]} and He is married')
