#Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. 
#The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. 
#In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
new_it_companies = {'Anthropic', 'OpenAI', 'GitHub'}
it_companies.update(new_it_companies)
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print(it_companies)

#What is the difference between remove and discard
#discard does not provide error if item does not exist

###Exercises: Level 2###

#Join A and B
joined_ab = A.union(B) #I prefer A|B
print(joined_ab)

#Find A intersection B
intersection_ab = A.intersection(B)
print(intersection_ab)

#Is A subset of B
A.issubset(B)

#Are A and B disjoint sets
A.isdisjoint(B)

#Join A with B and B with A
joined_ab = A.union(B)
joined_ba = B.union(A)

print(joined_ab)
print(joined_ba)

#What is the symmetric difference between A and B
A.symmetric_difference(B)

#Delete the sets completely
del(A)
del(B)


###Exercises: Level 3###

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(age)) #list length

age = set(age)

print(len(age)) #set length shorter

#Explain the difference between the following data types: string, list, tuple and set
#list: modifiable, ordered, can be empty, may have different data types
#tuple: immutable, ordered, have to change to list to change
#set: unordered, unindexed, distinct elements only, can use union, intersection, difference, symmetric difference, subset, superset, and disjoint


#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
split_sentence = sentence.split()
print(split_sentence)

sentence_set = set(split_sentence) # len = 12

print(len(sentence_set)) # len = 10


