from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        for key, value in ransomNote_counter.items():
            if magazine_counter[key]<value:
                return False
        return True

        
        
       