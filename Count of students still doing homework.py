class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        
        for ele1, ele2 in zip(startTime,endTime):
            if ele1 <= queryTime <= ele2:
                count+=1
        
        return count