class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        #declare a count
        count = 0
        
        #declare a trail
        trail = s[0].lower()
        
        #loop though s with the trail
        for ele in s[1:]:
            ele = ele.lower()
            if trail != ele:
                count+=1
            trail = ele
            
        #return the total count to finish the code
        return count