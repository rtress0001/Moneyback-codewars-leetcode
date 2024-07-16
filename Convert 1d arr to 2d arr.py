class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        #check if possible to create a 2 array
        if len(original) != m*n:
                return []
        
        #create a 2 array storage place
        arr = [[n] * n for i in range(m)]
        
        #loop though the spots in the array placing values in the right spot
        for i in range(m):
            for j in range(n):
                arr[i][j] = original[i*n+j]
        
        return arr
        
        
        
        