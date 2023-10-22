class Shape:
    def __init__(self):
        self.length = 0
        self.area = 0

    def area(self):
        return self.area

    class Square:
        def __init__(self, length):
            self.length = length

        def area(self):
            return self.length * self.length


l = int(input("Enter length of square: "))
print("Area of square is: ", Shape.Square(l).area())
