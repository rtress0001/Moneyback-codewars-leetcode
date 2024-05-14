class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n*(n+1)//2
        right = total
        left = 0
        for index in range(1,n+1):
            left+=index
            if right == left:
                return index
            right = total - left
        return -1
