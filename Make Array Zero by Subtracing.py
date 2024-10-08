class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        length = 0
        for ele in set(nums):
            if ele != 0:
                length+=1
        return length