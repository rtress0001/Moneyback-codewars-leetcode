from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        #create count dictionaries to find the number of occurances
        dict_count1 = Counter(words1)
        dict_count2 = Counter(words2)
        
        #intilize a counter
        count = 0
        
        
        for key in dict_count1:
            if dict_count1[key] == 1 and dict_count2[key] == 1:
                count+=1
        
        return count
           
        
        