from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        #intilize a counter
        count = 0
        
        #loop though the list
        for word in words:
                  
        #starts with function
            if s.startswith(word):
        #increment a counter
                count+=1
        return count

        
        