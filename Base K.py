def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        digit_sum = 0
        while n > 0:
            digit = n%k
            digit_sum += digit
            n//=k
        return digit_sum