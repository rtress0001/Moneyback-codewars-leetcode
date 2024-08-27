class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        num = original
        
        while num in nums:
            num *= 2
            
     
        return num
            