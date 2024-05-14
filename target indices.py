class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targets = []
        nums.sort()
        for index in range(len(nums)):
            if nums[index] ==target:
                targets.append(index)
        return targets