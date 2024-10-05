class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            sub = s[i:i+3]
            if len(set(sub))==3:
                count+=1
        
        return count
