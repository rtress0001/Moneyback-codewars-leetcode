def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arraytarget = []
        for nums, i in zip(nums,index):
            arraytarget.insert(i,nums)
        return arraytarget