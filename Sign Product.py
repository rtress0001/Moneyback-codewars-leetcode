    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for ele in nums:
            product *= ele
        if product > 0:
            return 1
        elif product == 0:
            return 0
        else:
            return -1