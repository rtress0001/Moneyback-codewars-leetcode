class Solution:
    def numWaterBottles(self, num_bottles: int, num_exchange: int) -> int:
        
        count = num_bottles
        while num_bottles >= num_exchange:
            new_bottles = num_bottles//num_exchange
            count+=new_bottles
            num_bottles=new_bottles+(num_bottles%num_exchange)
        
        return count