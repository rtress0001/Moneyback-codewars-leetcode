class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        #order by lowest frist
        prices.sort()
        
        #Declare a trailing pointer
        trail = prices[0]
        
        #Construct a loop that starts at the second to loop though the lowest
        for ele in prices[1:]:
            
            #conditional statement to select two chocolates
            if ele + trail <= money:
                return money - ele - trail
            trail = ele
            
        #if fail to find return the money
        return money
        