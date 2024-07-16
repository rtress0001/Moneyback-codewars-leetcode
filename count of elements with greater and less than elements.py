class Solution:
    def countElements(self, nums: List[int]) -> int:
        #nums has to be greater than 3 elements
        if len(nums) < 3:
            return 0
        
        #count intilizer
        count = 0
        #len of set short hand
        n = len(nums)
        
        
        #loop though the list in the iterator fasion
        for i in range(n):
            
            flag_smaller = False
            flag_larger = False
            
            #look for smaller
            for j in range(n):
                if i != j and nums[i]>nums[j]:
                    flag_smaller = True
                    break
            
            #look for bigger
            for j in range(n):
                if i != j and nums[i]<nums[j]:
                    flag_larger = True
                    break
            
            if flag_larger and flag_smaller:
                count+=1
        #return the count of elements that set off the conditions
        return count

                
                