class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        max_count = 0
        max_index = 0
        count = 0
        for i in range(len(mat)):
            count = mat[i].count(1)
            if count > max_count:
                max_count = count
                max_index = i
        
        return [max_index,max_count]