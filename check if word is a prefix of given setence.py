from typing import list

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        #index counter one index array
        i = 1
        
        #split the setence into a list
        lst = sentence.split()
        
        for ele in lst:
            if ele.startswith(searchWord):
                return i
            i+=1
        return -1