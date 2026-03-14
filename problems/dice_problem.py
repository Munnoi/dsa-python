class DiceProblem:
    def __init__(self, n):
        self.n = n

    def v1(self):
        if self.n == 1:
            print(6)
        elif self.n == 2:
            print(5)
        elif self.n == 3:
            print(4)
        elif self.n == 4:
            print(3)
        elif self.n == 5:
            print(2)
        else:
            print(1)

    def v2(self):
        print(7 - self.n)