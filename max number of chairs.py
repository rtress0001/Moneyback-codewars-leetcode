class Solution:
    def minimumChairs(self, s: str) -> int:
        
        #intilize a counter for people in the room
        count = 0
        max_count = 0
        
        #loop though the string
        for letter in s:
        
        
        #if coniditonal e or l
            if letter == "L":
                count-=1
                max_count = max(count,max_count)
            else:
                count+=1
                max_count = max(count,max_count)
            
        
        #return the count of people in the room
        return max_count
        
        
        
        
        
        