import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        max_num = max(nums)
        min_num = min(nums)
        return math.gcd(min_num,max_num)
            
        