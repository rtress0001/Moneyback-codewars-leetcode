class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_arr = sorted(heights)
        not_matching = []
        for i in range(len(heights)):
            if sorted_arr[i] != heights[i]:
                not_matching.append(i)
        return len(not_matching)