class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        
        count=0
        vowels = "aieou"
        for i in range(left, right+1):
            ele = words[i]
            if ele[0] in vowels and ele[-1] in vowels:
                count+=1
        return count