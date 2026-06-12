# Day 2: 30 days of pythong programming

#declare first name variable
first_name = 'Bruce'

#declare last name variable
last_name = 'Reyes'

#declare full name variable
full_name = first_name + ' ' + last_name

#declare a country variable
country = 'USA'

#declare a city variable
city = 'Waldorf'

#declare an age variable
age = 22

#declare an is_married variable
is_married = False

#declare an is_true Variable
is_male = True

#declare a is_light_on variable
is_light_on = True

#declare multiple variables in one line
fav_pokemon, fav_game, fav_movie, fav_food = 'Greninja', 'Destiny 2', 'Everything Everywhere All at Once', 'Fried Chicken'

###Exercise Level 2
#check all data types of declared variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_male))
print(type(is_light_on))

#find the length of first name 
len(first_name)

#compare the lengths of first and last name
print(len(first_name)-len(last_name))

#declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#add 
num_one + num_two

#subtract
num_one - num_two

#multiply
num_one * num_two

#divide(float)
num_one / num_two

#modulus and assign it to variable
remainder = num_one % num_two
print(remainder)

#find floor
floor = num_one // num_two
print(floor)

#The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.

r = 30
pi = 3.14

#area
area_of_circle = pi*r**2
print(area_of_circle)

#circumference
circum_of_circle = 2*pi*r
print(circum_of_circle)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("what is your first name?: ")
last_name = input("what is your last name?: ")
country = input("What country are you from?: ")
age = input("how old are you?: ")

print(first_name)
print(last_name)
print(country)
print(age)