from collections import Counter

class Solution:
    def checkString(self, s: str) -> bool:
        #flag for found b
        find_b = False
        
        for ele in s:
            if ele == 'b':
                find_b = True
            elif ele == 'a':
                if find_b:
                    return False
        return True
    