class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        n = len(nums)
        total = n * (n+1)//2
        return total-nums_sum