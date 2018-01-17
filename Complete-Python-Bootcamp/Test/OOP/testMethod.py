class Circle(object):

    #Class object attributes
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return (self.radius**2)*Circle.pi

    def setRadus(self, newRadius):
        self.radius = newRadius

    def get_radius(self):
        return self.radius

    def perimiter(self):
        return 2*Circle.pi*self.radius

c = Circle(radius = 10)
print(c.pi)
print(c.radius)
print('ares: ',c.area())
c.setRadus(20)
print(c.radius)
print('new ares: ',c.area())
print(c.get_radius())
print('parimeter: ',c.perimiter())