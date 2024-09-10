from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter_dict = Counter(nums)
        for key, value in counter_dict.items():
            if value > len(nums)/2:
                return key