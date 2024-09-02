class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        #create a set of the first oen
        set1 = set(nums[0])
        #find common elements of each set
        for ele in nums[1:]:
            set1.intersection_update(ele)
        #return to set sorted by ascending order  
        return sorted(set1)