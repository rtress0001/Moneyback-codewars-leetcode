class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        distance_value_count = 0
        for ele1 in arr1:
            flag = True
            for ele2 in arr2:
                if abs(ele1 - ele2) <= d:
                    flag = False
                    break
            if flag:
                distance_value_count += 1
                
        return distance_value_count