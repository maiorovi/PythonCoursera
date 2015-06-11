
class Rectangle:
    def square(self):
        return self.length * self.width
    pass

r = Rectangle()
r.width, r.length = 2,5
print r.square()

# Point.x = 1
# Point.y = 3
