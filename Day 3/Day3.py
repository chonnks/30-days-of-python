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
slope_2 = 