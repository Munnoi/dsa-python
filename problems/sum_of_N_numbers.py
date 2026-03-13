class SumOfNNumbers:
    def __init__(self, n):
        self.n = n

    def v1(self):
        sum = 0
        for i in range(1, self.n + 1):
            sum += i
        print(sum)

    def v2(self):
        print(self.n * (self.n + 1) // 2)