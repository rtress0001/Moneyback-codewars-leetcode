class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        
        #create counter for the grid to label positions
        position_counter = 0
        
        #gird
        grid = []
        row = []
        #for loop to create a grid
        for i in range(n):
            for j in range(n):
                row.append(position_counter)
                position_counter+=1
            grid.append(row)
            row = []
        
        #reuse variable for commands
        x_pos, y_pos = 0,0
        
        for command in commands:
            if command == "UP":
              
                    x_pos -= 1
            elif command == "DOWN":
                
                    x_pos += 1
            elif command == "LEFT":
               
                    y_pos -= 1
            elif command == "RIGHT":
                
                    y_pos += 1
            
        return grid[x_pos][y_pos]
                
        
                