class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return "b"*n
        else:
            return "b" + "c"*(n-1)