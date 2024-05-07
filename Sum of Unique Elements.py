class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sum_unique = sum(num for num, count in counts.items() if count == 1)
        return sum_unique
