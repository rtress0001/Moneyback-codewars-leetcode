class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def selfdividing(num):
            for ele in str(num):
                if ele == "0" or num%int(ele) != 0:
                    return False
            return True
        
        
        lst_selfdividing = []
        for num in range(left,right+1):
            if selfdividing(num):
                lst_selfdividing.append(num)
            
        return lst_selfdividing
                    
                
 