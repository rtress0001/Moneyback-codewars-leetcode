class Solution:
    def countAsterisks(self, s: str) -> int:
        between = False
        count = 0
        for ele in s:
            if ele == "|":
                between = not between
            elif ele == "*" and not between:
                count+=1
        
        return count