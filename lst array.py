class Solution:
    def makeGood(self, s: str) -> str:
        
        lst = list(s)
        i = 0
        
        while i < len(lst) - 1:
            if abs(ord(lst[i]) - ord(lst[i + 1])) == 32:
                lst = lst[:i] + lst[i+2:]  
                if i > 0:
                    i -= 1  
            else:
                i += 1
        
        return "".join(lst)