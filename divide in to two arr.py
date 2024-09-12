class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        
        arr1.append(nums[0])
        arr2.append(nums[1])
        
        for ele in nums[2:]:
            if arr1[-1] >= arr2[-1]:
                arr1.append(ele)
            else:
                arr2.append(ele)
        
        return arr1 + arr2
    