class Solution:
    def greatestLetter(self, s: str) -> str:
        char = set(s)
        
        for i in range(ord("Z"),ord("A")-1,-1):
            if chr(i) in char and chr(i).lower() in char:
                return chr(i)
        return ""