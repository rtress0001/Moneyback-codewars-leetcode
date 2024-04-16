class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        trail = 0
        for lead in range(len(nums)):
            if nums[lead] != val:
                nums[trail] = nums[lead]
                trail +=1
        return trail