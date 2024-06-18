class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        lst = []
        for ele in nums:
            if nums.count(ele) == 1:
                lst.append(ele)
        return lst
                
        