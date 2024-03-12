 def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        trail = 0
        
        for index in range(1,len(nums)):
            if nums[index] != nums[trail]:
                trail += 1
                nums[trail] = nums[index]
        
        return trail + 1
