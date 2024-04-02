    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        hashsum = 0
        for ele in str(x):
            hashsum += int(ele)
        if x%hashsum == 0:
            return hashsum
        else:
            return -1