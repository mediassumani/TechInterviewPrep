    def myPow(self, x, n):
        # Base Case
        if n == 1:
            return x
        if n == 0:
            return 1
        
        # Recursive Case
        if n > 0:
            # for positive integers
            return self.myPow(x, n-1) * x
        elif n < 0:
            # for negative integers
            return self.myPow(1/x, n-1)
