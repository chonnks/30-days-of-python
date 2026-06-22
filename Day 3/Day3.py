# declare your age as an integer variable
age = 22

# declare your height as a float variable 
height = 5.9

# declare a variable that stores a complex number
complex  = 1j

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
tri_base = float(input("Enter base: ")) #has to be float
tri_height = float(input("Enter height: "))
tri_area = 0.5 * tri_base * tri_height

print("The area of the triangle is " + str(tri_area)) # has to be a string when doing concatenation

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter side a:"))
side_b = float(input("Enter side b:"))
side_c = float(input("Enter side c:"))

perimeter = side_a + side_b + side_c

print("The perimeter of the triangle is " + str(perimeter))

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rect_area = length * width
rect_perimeter = 2 * (length + width)

print(rect_area)
print(rect_perimeter)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter the radius of the circle: "))
pi = 3.14

circ_area = pi * 2 * radius
circ_circumference = 2 * pi * radius 

print(circ_area)
print(circ_circumference)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
x_int = 1 
y_int = -2

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope_2 = (10-2)/(6-2)
euclidean_dist = (((2-6)**2)+((2-10)**2))**0.5

print(euclidean_dist)
print(slope_2)

#compare both slopes
slopes_comp = slope_2 - float(slope)
print(slopes_comp)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
#y is 0 at -3

0 == ((-3)**2 +6*(-3)+9)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_len = len('python')
dragon_len = len('dragon')

python_len == dragon_len

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon') #Take note of how this is done

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('on' in 'I hope this course is not full of jargon')

#Find the length of the text python and convert the value to float and convert it to string
print(float(len('python')))
print(str(len('python')))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# how to check: num % 2 == 0

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor = 7//3
print(floor)

#Check if type of '10' is equal to type of 10
print(type(10))
print(type('10'))

#Check if int('9.8') is equal to 10
int('9.8')

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours =(float(input('Enter your hours per week: ')))
rate = (float(input('Enter rate per hour: ')))

earning = hours * rate

print(" Your weekly earning is: " + str(earning))

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = (float(input('Enter the number of years: ')))
seconds = float(31536000)

years_person_lives = years * seconds

print('You have lived for ' + str(years_person_lives) + ' seconds.')


#Write a Python script that displays the following table
table = "1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125"

print(table)