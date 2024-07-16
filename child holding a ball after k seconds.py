class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        
       #place of ball 
        ball = 0
        #directionalty flag
        direction = 1
        
        for i in range(k):
            ball += direction
            
            #Direction swapping conditions
            if ball == 0:
                direction = 1
            if ball == n-1:
                direction = -1
                
        return ball
                