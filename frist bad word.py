# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left_bin = 1
        right_bin = n
    
        while left_bin < right_bin:
            mid = (left_bin + right_bin) // 2
            if isBadVersion(mid):
                right_bin = mid
            else:
                left_bin = mid + 1 
        return left_bin