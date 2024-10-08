class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        #intilize a counter for time
        count_time = 0
        
        for i in range(len(tickets)):
            if i <= k:
                count_time += min(tickets[i],tickets[k])
            else:
                count_time += min(tickets[i],tickets[k]-1)
        
        return count_time

            