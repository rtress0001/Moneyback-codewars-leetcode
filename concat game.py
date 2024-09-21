class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        
        temp = 0
        con = 0
        while len(nums)>1:
            temp = int(str(nums[0])+str(nums[-1]))
            nums.pop(0)
            nums.pop(-1)
            con+=temp
        if nums:
            con+=nums[0]

        return con