class SwapTwoNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def v1(self):
        temp = self.a
        self.a = self.b
        self.b = temp
        print(f"a: {self.a}, b: {self.b}")

    def v2(self):
        self.a, self.b = self.b, self.a
        print(f"a: {self.a}, b: {self.b}")
