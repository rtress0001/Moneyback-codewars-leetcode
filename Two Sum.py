 def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for trail in range(len(nums)):
            for i in range(trail +1, len(nums)):
                if nums[i] + nums[trail] == target:
                    return [i,trail]
         
            