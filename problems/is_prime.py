class IsPrime:
    def __init__(self, n):
        self.n = n

    def v1(self):
        is_prime = True

        if self.n <= 1:
            is_prime = False

        for i in range(2, int(self.n ** 0.5) + 1):
            if self.n % i == 0:
                is_prime = False
                break

        if is_prime:
            print("Prime")
        else:
            print("Not Prime")

