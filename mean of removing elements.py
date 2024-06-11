class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        n=n//20
        arr.sort()
        for i in range(n):
            arr.pop(0)
            arr.pop(-1)
        return sum(arr)/len(arr)
        