class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_fives = 0
        count_tens = 0
        for ele in bills:
            if ele == 5:
                count_fives += 1
            elif ele == 10:
                if count_fives == 0:
                    return False
                count_tens +=1
                count_fives -=1
            else:
                if count_fives>0 and count_tens > 0:
                    count_tens -=1
                    count_fives -=1
                elif count_fives>=3:
                    count_fives-=3
                else:
                    return False
                
        return True
