class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        #initate a pointer amd counter
        
        counter = 0
        j = 1
        #double loop though the array with a trail
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
            
                #check if coniditon is meet
                if nums[i] == nums[j] and (i*j) % k == 0:
                    #increment counter
                    counter +=1
            
        #return the equal and divisable
        return counter
        