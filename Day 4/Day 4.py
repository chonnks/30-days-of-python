# Strings

# In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision

# Strings only
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
thirty = 'Thirty'
days = ' Days'
of = ' Of'
python = ' Python'

full_concat = thirty + days + of + python
print(full_concat)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding = 'Coding'
string_for = ' For'
string_all = ' All'

full_concat_2 = coding + string_for + string_all
print(full_concat_2)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

#print the variable company using print().
print(company)

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
print(len(company))
for_all = company[7:14]

print(for_all)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))

#Replace the word coding in the string 'Coding For All' to Python
company = (company.replace('Coding', 'Python'))
print(company)

#Change "Python for All" to "Python for Everyone" using the replace method or other methods.
company = (company.replace('All', 'Everyone'))
print(company)

#Split the string 'Coding For All' using space as the separator (split()) .
company = 'Coding For All'
print(company.split())

#Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
faang = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(faang.split())

#What is the character at index 0 in the string Coding For All.
print(company.index('C'))

#What is the last index of the string Coding For All.
print(len(company)-1)

#What character is at index 10 in "Coding For All" string.
index_find = company[10]
print(index_find)

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
pfe = 'Python For Everyone'

#Create an acronym or an abbreviation for the name 'Coding For All'.
cfa = 'Coding For All'

#Use index to determine the position of the first occurrence of C in Coding For All.
print(cfa.index('C'))

#Use index to determine the position of the first occurrence of F in Coding For All.
print(cfa.index('F'))


#Use rfind to determine the position of the last occurrence of l in Coding For All People.
cfap = 'Coding For All People'
print(cfap.rfind('l'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(len(sentence))

first_part_sentence = sentence[0:30]
print(first_part_sentence)
second_part_sentence = sentence[54:71]
print(second_part_sentence)

new_sentence = first_part_sentence + second_part_sentence

print(new_sentence)

#Does 'Coding For All' start with a substring Coding?
print(cfa.startswith('Coding'))

#Does 'Coding For All' end with a substring coding?
print(cfa.endswith('Coding'))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
cfa_spaces = '   Coding For All   '
print(cfa_spaces.strip('   '))

#Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython or thirty_days_of_python
string_one = '30DaysOfPython'
string_two = 'thirty_days_of_python'

print(string_one.isidentifier())
print(string_two.isidentifier())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
random_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joining = '# '.join(random_list)

print(joining)

#Use the new line escape sequence to separate the following sentences: I am enjoying this challenge.I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

#Use a tab escape sequence to write the following lines: Name      Age     Country   City and Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity\nReyes\t250\tAmerica\tMaryland')

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
formatted_string = 'The area of a circle with a radius %d is %d meters square' %(radius, area)

print('radius = 10\npi = 3.14\n area = pi * radius ** 2\n' + formatted_string)


#Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')