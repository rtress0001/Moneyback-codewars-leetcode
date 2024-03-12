def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count_arr = []
        count = 0
        for index in range(len(nums)):
            for jndex in range(len(nums)):
                if nums[index] != nums[jndex] and nums[index]>nums[jndex]:
                    count += 1
            count_arr.append(count)
            count = 0
        return count_arr
        