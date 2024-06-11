class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        postion = 0
        count = 0
        for ele in nums:
            postion += ele
            if postion == 0:
                count+=1
        return count
        