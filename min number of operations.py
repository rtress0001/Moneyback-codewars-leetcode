class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for ele in nums:
            if ele >= k:
                count +=1
        return len(nums) - count
                