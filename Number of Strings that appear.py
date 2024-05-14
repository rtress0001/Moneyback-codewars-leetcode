class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for ele in patterns:
            if word.count(ele):
                count+=1
        return count