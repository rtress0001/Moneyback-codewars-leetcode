class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_bin = 0
        right_bin = len(nums) - 1
    
        while left_bin <= right_bin:
            mid = (left_bin + right_bin) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left_bin = mid + 1
            else:
                right_bin = mid - 1
    
        return left_bin