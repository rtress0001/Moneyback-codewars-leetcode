class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        #convert to sets
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        
        #find the common elements between all the posstible sets
        union1 = set1.intersection(set2)
        union2 = set2.intersection(set3)
        union3 = set1.intersection(set3)
        
        
        #find the union of the 3 sets 
        return union1 | union2 | union3