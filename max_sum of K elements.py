class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        ret = 0
        max_num = 0
        for i in range(k):
            if not nums:
                break
            max_num = nums.pop(0)
            nums.append(max_num+1)
            ret += max_num
            nums.sort(reverse=True)
        return ret