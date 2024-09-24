class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        
        for ele in nums:
            
            if ele < min_price:
                min_price = ele
                
            elif ele - min_price > max_profit:
                max_profit = ele - min_price
            
        if max_profit > 0:
            return max_profit
        else:
            return -1
            