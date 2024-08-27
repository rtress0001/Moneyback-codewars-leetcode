class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        
        split_singles = []
        split_doubles = []
        
        for num in nums:
            if len(str(num)) == 1:
                split_singles.append(num)
            else:
                split_doubles.append(num)
        if sum(split_singles) != sum(split_doubles):
            return True
        else:
            return False