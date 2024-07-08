class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        #counter of operations
        count = 0
        #loop though the list to change each element
        for i in range(len(nums)):
            remainder = nums[i]%3
            #check if divisable by 3
            if remainder != 0:
                #count operational changes
                count += 1
                 #change it to make it divisable by 3
                nums[i] = nums[i]+remainder
        
        #return the number of operations
        return count