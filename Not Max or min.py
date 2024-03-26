 def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return -1
        non_max_min = []
        for ele in nums:
            if ele == max(nums) or ele == min(nums):
                pass
            else:
                non_max_min.append(ele)
        return non_max_min[0]
        