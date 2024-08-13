class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        #intitlize a counter 
        unique_lst = []
        #loop though the list
        
        for ele in word:
            if ele.islower():
                if ele.upper() in word:
                    unique_lst.append(ele) 
        
        return len(set(unique_lst))
        