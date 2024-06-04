class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        changes = 0
        count = 0
        n = len(s)-1
        s = list(s)
        for index in range(len(s)//2):
            if s[n] != s[count]:
                if s[n]>s[count]:
                    s[n] = s[count]
                else: 
                    s[count] = s[n]
            n-=1
            count+=1
        return "".join(s)
            