from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count_nums = Counter(nums)
        
        for count in count_nums.values():
            if count %2 != 0:
                return False
        return True