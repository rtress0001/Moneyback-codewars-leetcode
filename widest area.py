class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        
        width = 0
        max_width = 0
        trail = 0
        for index in range(len(points)-1):
            width = points[index+1][0] - points[index][0]
            max_width = max(max_width,width)
    
        return max_width