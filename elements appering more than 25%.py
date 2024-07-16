from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        Counter_dict = Counter(arr)
        for key, value in Counter_dict.items():
            if value > len(arr)/4:
                return key
        return -1
                
        
        