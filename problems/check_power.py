import math

class CheckPower:
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def v1(self):
        if self.p == 1:
            print("True")
            return

        while self.n % self.p == 0:
            self.n //= self.p

        if self.n == 1:
            print("True")
        else:
            print("False")

    def v2(self):
        if self.p == 1:
            print("True")
            return

        pow = 1
        while pow < self.n:
            pow *= self.p

        if pow == self.n:
            print("True")
        else:
            print("False")