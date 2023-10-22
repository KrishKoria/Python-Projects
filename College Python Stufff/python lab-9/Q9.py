class Person:
    def __init__(self):
        pass


class Male(Person):
    def __init__(self):
        super().__init__()
        self.gender = "Male"

    def getGender(self):
        print(self.gender)


class Female(Person):
    def __init__(self):
        super().__init__()
        self.gender = "Female"

    def getGender(self):
        print(self.gender)
