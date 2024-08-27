from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums)//2
        element = 0
        for key, value in counter.items():
            if value == n:
                return key
        
        