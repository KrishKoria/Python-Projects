class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


obj = Circle(float(input("Enter radius of circle: ")))
print(obj.area())
