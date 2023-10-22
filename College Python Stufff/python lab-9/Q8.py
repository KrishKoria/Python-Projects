class StringStuff:
    def __init__(self):
        self.my_string = ""

    def getString(self):
        self.my_string = input("Enter a string: ")

    def printString(self):
        print(self.my_string.upper())


def testFunction():
    my_string = StringStuff()
    my_string.getString()
    my_string.printString()


if __name__ == "__main__":
    testFunction()
