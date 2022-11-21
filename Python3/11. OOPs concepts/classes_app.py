# Classes - blueprints of objects

class Point: # Pascal case for classes
    def __init__(self, x, y): #constructor
        self.x = x # self is a reference to the current object
        self.y = y
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")

point1 = Point(10, 20)
point1.draw()
point1.move()
print(point1.x)