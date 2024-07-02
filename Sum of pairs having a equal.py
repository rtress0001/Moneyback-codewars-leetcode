class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        #declare a set
        sum_set = set()
        
        #loop though the list using a leader pointer
        lead = 0
        for i in range(len(nums)-1):
            #check if the sums is in the set?
            if nums[i]+nums[i+1] in sum_set:
                return True
            
            else:
                sum_set.add(nums[i]+nums[i+1])
        
        #checked the whole lst must be false
        return False
        
        