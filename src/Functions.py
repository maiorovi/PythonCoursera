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