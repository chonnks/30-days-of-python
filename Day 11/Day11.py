# Functions
# So far we have seen many built-in Python functions. In this section, we will focus on custom functions. What is a function? Before we start making functions, let us learn what a function is and why we need them?

# Defining a Function
# A function is a reusable block of code or programming statements designed to perform a certain task. To define or declare a function, Python provides the def keyword. The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.

# Declaring and Calling a Function
# When we make a function, we call it declaring a function. When we start using the it, we call it calling or invoking a function. Functions can be declared with or without parameters.

#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(x, y):
    result = x + y
    return result
print(add_two_numbers(x=1, y=2))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(pi, r):
    area = pi * (r*r)
    return area
print(area_of_circle(pi = 3.14, r = 1))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for i in args:
        if not isinstance(i,(int, float)):
            return f"Error: {item!r} is not a number (got type{type(i).__name__})"
        total += i
    return total
print(add_all_nums(1,2,3))

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def celsius_to_fahrenheit(c):
    f = c * (9/5) + 32
    return f
print(celsius_to_fahrenheit(0))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month == 'December' or month == 'January' or month == 'February':
        season = 'Winter'
    elif month == 'March' or month == 'April' or month == 'May':
        season = 'Spring'
    elif month == 'June' or month == 'July' or month == 'August':
        season = 'Summer'
    else:
        season = 'Autumn'
    return season
print(check_season('September'))

# Write a function called calculate_slope which return the slope of a linear equation
def calc_slope(x,y):
    slope = y/x
    return slope
print(calc_slope(x=2,y=3))

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        if b == 0:
            return "No solution (not an equation)" if c != 0 else "Infinite solutions"
        return (-c / b,)  # linear equation: bx + c = 0
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        real_part = -b / (2*a)
        imag_part = (-discriminant)**0.5 / (2*a)
        return (complex(real_part, imag_part), complex(real_part, -imag_part))
    
print(solve_quadratic_eqn(1,2,1))




