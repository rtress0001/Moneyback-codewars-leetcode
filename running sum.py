def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = []
        for index in range(len(nums)):
            sums.append(sum(nums[:index+1]))
        return sums