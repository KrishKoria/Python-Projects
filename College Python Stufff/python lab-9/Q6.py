class Generator:
    def __init__(self, n):
        self.n = n

    def generate(self):
        for i in range(0, self.n + 1):
            if i % 7 == 0:
                yield i


print([i for i in Generator(int(input("Enter a number: "))).generate()])
