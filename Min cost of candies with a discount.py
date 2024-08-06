class Solution:
    def minimumCost(self, cost: List[int]) -> int:
      
        cost.sort(reverse=True)
        #sum costs
        sum_cost = 0
        
        lst_of_three = []
        
        for i in range(len(cost)):
            sum_cost+=cost[i]
            lst_of_three.append(cost[i])
            if len(lst_of_three) == 3:
                sum_cost -= min(lst_of_three)
                lst_of_three = []
            
        return sum_cost
                
        