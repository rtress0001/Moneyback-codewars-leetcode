from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        #create a dictionary of number of times each charater occurs
        freq_char = Counter(s)
        
        #sort the list by the frequency of occurance
        sorted_lst = sorted(freq_char.items(), key = lambda x: (-x[1],x[0]))
        
        ret = ""
        for ele in sorted_lst:
            ret+=ele[0]*ele[1]
        
        return ret
        
        