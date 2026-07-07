# There are four collection data types in Python :

# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
# Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
# Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
# Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
# list can be made a  few ways :
#lst = list()
#lst = []



#Exercises
#Declare an empty list
lst = []

#Declare a list with more than 5 items
pokemon = ['Greninja', 'Infernape', 'Charizard', 'Garchomp', 'Gengar']
print(pokemon)

#Find the length of your list
print(len(pokemon))

#Get the first item, the middle item and the last item of the list
first_item, second_item, third_item, fourth_item, fifth_item = pokemon

print(first_item)
print(third_item)
print(fifth_item)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ('Bruce', 22, 5.9, 'single', '123 Address Road')

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))
first_company, second_company, third_company, fourth_company, fifth_company, sixth_company, seventh_company = it_companies

#Print the first, middle and last company
print(first_company)
print(fourth_company)
print(seventh_company)

#Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert(2, 'Netflix')
print(it_companies)

#Join the it_companies with a string '#;  '
new_it_companies ='#; '.join(it_companies)
print(new_it_companies)

#Check if a certain company exists in the it_companies list.
does_exist = 'Google' in it_companies
print(does_exist)

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list
first_three = it_companies[0:3]
print(first_three)

#Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

#Slice out the middle IT company or companies from the list
middle_companies = it_companies[3:5]
print(middle_companies)

#Remove the first IT company from the list
del it_companies[0]
print(it_companies)

#Remove the middle IT company or companies from the list
del it_companies[4]
print(it_companies)

#Remove the last IT company from the list
del it_companies[5]
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
del it_companies
print(it_companies)

#Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, 'Python')
full_stack.insert(5,'SQL')

print(full_stack)


### EXERCISE LEVEL 2 ###
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
print(ages)

#Add the min age and the max age again to the list
ages.insert(0, 19)
ages.insert(-1, 26)
del ages[0]

print(ages)

#Find the median age (one middle item or two middle items divided by two)
ages_median_1 = ages[5] + ages[6]
ages_median = ages_median_1/2

print(ages_median)

#Find the average age (sum of all items divided by their number )
ages_sum = ages[0] + ages[1] + ages[2] + ages[3] + ages[4] + ages[5] + ages[6] + ages[7] + ages[8] + ages[9] + ages[10] + ages[11]
ages_avg = ages_sum / len(ages)

print(ages_avg)

#Find the range of the ages (max minus min)
ages_range = ages[11] - ages[0]

print(ages_range)


#Compare the value of (min - average) and (max - average), use abs() method
minimum = min(ages)
maximum = max(ages)

average = sum(ages) / len(ages)

min_diff = abs(minimum - average)
max_diff = abs(maximum - average)

print(min_diff)
print(max_diff)

print(min_diff > max_diff)

#Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]


#Find the middle country(ies) in the countries list
print(len(countries)/3)
print(65*2)


middle_countries = countries[65:130]
print(middle_countries)
print(len(middle_countries))

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(len(countries)/2)

first_half = countries[0:97]
second_half = countries[98:195]

print(len(first_half))
print(len(second_half))

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_short = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia , usa, *scandic = countries_short

print(china)
print(scandic)