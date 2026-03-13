class MultiplicationTable:
    def __init__(self, num):
        self.num = num

    def v1(self):
        for i in range(1, 11):
            print(f"{self.num} * {i} = {self.num * i}")