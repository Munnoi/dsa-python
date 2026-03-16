class ReverseDigits:
    def __init__(self, n):
        self.n = n

    def v1(self):
        reversed_num = 0
        while self.n:
            reversed_num = reversed_num * 10 + self.n % 10
            self.n //= 10
        print(reversed_num)

    def v2(self):
        reversed_num = int(str(self.n)[::-1])
        print(reversed_num)

    def v3(self):
        s = list(str(self.n))
        s.reverse()
        print(int(''.join(s)))