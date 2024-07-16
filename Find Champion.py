class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        
        #intilize a storage space for champion
        champion = 0
        
        #loop though the gird
        
        for i in range(len(grid)):
            if grid[champion][i] == 0:
                champion = i
                
        for i in range(len(grid)):
            if i != champion and grid[i][champion] == 1:
                return 0
            
        return champion
    
        
        