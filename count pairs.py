class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        pairs = []
        for index in range(len(nums)):
            for jndex in range(index,len(nums)):
                if abs(nums[index] - nums[jndex]) == k:
                    pairs.append(True)
        return len(pairs)