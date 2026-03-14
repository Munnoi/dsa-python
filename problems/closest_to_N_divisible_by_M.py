class ClosestToNDivisibleByM:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    '''
    We first compute the quotient q = n / m, then calculate two candidates:

    - n1 = m * q
        This is the closest multiple of m that is less than or equal to n.

    - n2 = m * (q + 1) or m * (q - 1)
        We choose q + 1 or q - 1 based on the signs of n and m:
            - If n and m have the same sign, use n2 = m * (q + 1)
                This moves in the direction toward n, getting the next closest multiple above n.
            - If n and m have opposite signs, use n2 = m * (q - 1)
                This accounts for the fact that increasing q would move away from n due to the sign flip, so we instead go backward to get the next closest multiple.

    Then we return the one (n1 or n2) that has the smaller absolute difference from n.
    If both have the same distance from n, return the one with the greater absolute value, as required. 
    '''

    def v1(self):
        q = int(self.n / self.m)
        n1 = self.m * q
        
        if (self.n * self.m) > 0:
            n2 = self.m * (q + 1)
        else:
            n2 = self.m * (q - 1)
            
        if abs(self.n - n1) < abs(self.n - n2):
            print(n1)
        else:
            print(n2)

    def v2(self):
        closest = 0
        min_difference = float('inf')

        for i in range(self.n - abs(self.m), self.n + abs(self.m) + 1):
            if i % self.m == 0:
                difference = abs(i - self.n)
                if difference < min_difference or (difference == min_difference and abs(i) > abs(closest)):
                    closest = i
                    min_difference = difference

        print(closest)