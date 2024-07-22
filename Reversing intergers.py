class Solution:
class Solution:
    def reverse(self, x: int) -> int:
        
        if x > 0:
            string = str(x)
            string = string[::-1]
            x = int(string)
        if x < 0:
            x*=-1
            string = str(x)
            string = string[::-1]
            x = -1*int(string)
        
        if x == 0 or x < -2**31 or x > 2**31 - 1:
            return 0
        
        return x
        