class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_small = set(allowed)
        fitler = []
        count = 0 
        for ele in words:
            if all(ele2 in allowed_small for ele2 in ele):
                count +=1
        return count