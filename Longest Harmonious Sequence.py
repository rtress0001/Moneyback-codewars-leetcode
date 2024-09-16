from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count_items = Counter(nums)
        max_length = 0
        for key, value in count_items.items():
            if key + 1 in count_items:
                max_length = max(max_length,count_items[key]+count_items[key+1])
        return max_length
            