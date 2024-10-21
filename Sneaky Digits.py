from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count_nums = Counter(nums)
        return_list = []
        for key,value in count_nums.items():
            if value == 2:
                return_list.append(key)
        return return_list