class Solution:
    def maxPower(self, s: str) -> int:
        
        #intitize a counter
        count = 1
        max_count = 0
        #intilize a trail
        trail = s[0]
        if len(s) == 1:
            return 1
        for letter in s[1:]:
            if trail == letter:
                count += 1
            else:
                count=1
            max_count=max(count,max_count)
            trail = letter
        return max_count
        
            
        
        