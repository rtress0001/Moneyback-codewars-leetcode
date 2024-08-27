class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        english_only = ""
        for ele in s:
            if ele.isalpha():
                english_only+=ele
        
        ret = ""
        english_only = english_only[::-1]
        i = 0
        for ele in s:
            if ele.isalpha():
                ret+=english_only[i]
                i+=1
            else:
                ret+=ele
            
        
        return ret