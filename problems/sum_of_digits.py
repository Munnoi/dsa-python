class SumOfDigits:
    def __init__(self, n):
        self.n = n 

    def v1(self):
        sum = 0
        for digit in str(self.n):
            sum += int(digit)
        print(sum)

    def v2(self):
        sum = 0
        while self.n:
            sum += self.n % 10
            self.n //= 10
        print(sum)