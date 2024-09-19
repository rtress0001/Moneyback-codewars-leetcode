class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices_dict  = {}
        
        for i, ele in enumerate(nums):
            if ele in indices_dict and i - indices_dict[ele] <= k:
                return True
            indices_dict[ele] = i
        return False
