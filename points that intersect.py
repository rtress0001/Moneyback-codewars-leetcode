class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = set()
        for frist, last in nums:
            for point in range(frist,last+1):
                points.add(point)
                
        return len(points)