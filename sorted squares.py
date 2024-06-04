class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        for ele in nums:
            squares.append(ele*ele)
        squares.sort()
        return squares
        