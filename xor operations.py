class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor_return = 0
        num = 0
        for index in range(n):
            num = start + 2 * index
            xor_return ^= num
        return xor_return
            