class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        count = 0
        for ele in arr:
            if arr.count(ele) == 1:
                count+=1
                if count == k:
                    return ele
        return ""
        