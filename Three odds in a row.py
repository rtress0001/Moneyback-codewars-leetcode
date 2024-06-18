class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        if len(arr) <= 2:
            return False
        
        trail = arr[0]
        lead = arr[2]
        for index in range(1,len(arr)-1):
            if trail % 2 == 1 and arr[index]%2 == 1 and lead%2 == 1:
                return True
            trail = arr[index]
            lead = arr[index+1]
        
        return False
            