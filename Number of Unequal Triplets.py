class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        
        #intitlize a counter
        count = 0
        
        #create a triple loop that creats triplets
        
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count+=1
        return count