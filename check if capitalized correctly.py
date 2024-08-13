class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #if statement removing coniditons
        if word.isupper() or word.islower():
            return True
        #if statement for final condition
        if word[0].isupper() and word[1:].islower():
            return True
        #fall back false
        return False