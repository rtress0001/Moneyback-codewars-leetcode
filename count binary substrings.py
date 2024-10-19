class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        bins = []
        count = 1
        
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                bins.append(count)
                count = 1
                
        bins.append(count)
        
        test = 0
        for i in range(1,len(bins)):
            test += min(bins[i-1],bins[i])
        
        return test
    