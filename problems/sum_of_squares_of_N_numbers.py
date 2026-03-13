class SumOfSquaresOfNNumbers:
    def __init__(self, n):
        self.n = n

    def v1(self):
        sum_sq = 0
        for i in range(1, self.n + 1):
            sum_sq += i * i
        print(sum_sq)

    def v2(self):
        print(self.n * (self.n + 1) * (2 * self.n + 1) // 6)
