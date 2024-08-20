class Solution:
    def isHappy(self, n: int) -> bool:
        
        #track if it loops endlessly
        set_of_seen = set()
      
        
        #loop though each digit
        while n != 1 and n not in set_of_seen:
            #add a seen to the set
            set_of_seen.add(n)
            #reset sum nums
            sum_nums = 0
            #loop though each digit to sum of the digits
            for ele in str(n):
                #sum of squares
                sum_nums += int(ele) ** 2
            #store new n
            n = sum_nums
        #check if the end result is n to be happy
        return n == 1