#functions computes area of a triangle
def triangle_area(base, height) :
    area = (1.0 / 2) * base * height
    return  area

def factorial(number):
    f = 1
    if number == 0:
        return 1
    return number * factorial(number - 1)

def hello():
    print "Hello world"
    return None

print triangle_area(4,5)

print factorial(5)

hello()

p = False
q = False
print not (p or not q)

def do_stuff():
    print "Hello world"
    return "Is it over yet?"
    print "Goodbye cruel world!"

print do_stuff()
print()

n = 123;
print(n // 10) % 10

print (n % 100 - n % 10) / 10

print (n % 10) / 10

print 2 ** 5
x=2

print -5*(x ** 5) + 69*(x ** 2) - 47

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

import math

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

project_to_distance(2, 7, 4)


def square(sides_number, lenght):
    square = 0.25 * sides_number * (lenght ** 2) / math.tan(math.pi / sides_number)
    return square


print square(7, 3)

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value* (1 + rate_per_period) ** periods

    # Put your code here.
print  future_value(500, .04, 10, 10)
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)