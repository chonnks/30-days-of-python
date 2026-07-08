# A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# + operator: to join two or more tuples and to create a new tuple


#Create an empty tuple
empty_tuple = ()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
siblings = ('Sophia', 'Kendrick', 'Maddie')

#Join brothers and sisters tuples and assign it to siblings
brothers = ('Miko', 'Chris', 'Riley')
sisters = ('Jess', 'Lani', 'Lisa')

full_fam = siblings + brothers + sisters

#How many siblings do you have?
print(len(full_fam))
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)

family_members.insert(0, 'Roberto')
family_members.insert(0, 'Marilyn')

print(family_members)

family_members = tuple(family_members)

###Exercises Level 2###

#Unpack siblings and parents from family_members
mom = family_members[0]
dad = family_members[1]
pia = family_members[2]
ken = family_members[3]
mad = family_members[4]

print(mom)
print(dad)
print(pia)
print(ken)
print(mad)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Mango', 'Banana', 'Watermelon')
vegetables = ('Lettuce', 'Broccoli', 'Corn')
animals = ('Dogs', 'Bears', 'Otter')

food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items = food_stuff_tp[3:6]
print(middle_items)

#Slice out the first three items and the last three items from food_stuff_lt list
first_items = food_stuff_tp[0:3]
last_items = food_stuff_tp[-3:]

print(first_items)
print(last_items)

#Delete the food_stuff_tp tuple completely
del(food_stuff_tp)

#Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

'Estonia' in nordic_countries
'Iceland' in nordic_countries




