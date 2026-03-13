class EvenOrOdd:
    def __init__(self, num):
        self.num = num

    def v1(self):
        if self.num % 2:
            print("Odd")
        else:
            print("Even")

    def v2(self):
        if self.num & 1:
            print("Odd")
        else:
            print("Even")