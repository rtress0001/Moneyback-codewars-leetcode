class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        
        #find diminison of the grid
        m = len(grid)
        n = len(grid[0])
        
        
        #create a double loop
        for i in range(m):
            for j in range(n):
                #check if the one below is equal to value in grid
                if i+1 < m and grid[i][j] != grid[i+1][j]:
                    return False
                    
        
        
                #check if the one to left is differ to value in the grid
                if j+1 < n and grid[i][j] == grid[i][j+1]:
                    return False
                        
        
        
        return True
        