from collections import Counter

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count_dict = Counter(nums)
        
        ret = 0
        for key, value in count_dict.items():
            if value == 2:
                ret ^= key
        
        return ret