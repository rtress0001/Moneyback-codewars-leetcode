class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        #string storage 
        number_letters = ""

        #convert letters into numbers
        for ele in s:
            number_letters += str(ord(ele) - ord('a') + 1)
        
        #loop though the sum k times
        for i in range(k):
            #reset the num sum every loop
            sum_nums = 0
            #sum all the digits for each iteration
            for ele in number_letters:
                #make a list of digits to be sum
                sum_nums += int(ele)
            #set the group to be a string after summing
            number_letters = str(sum_nums)
        #convert back to int    
        return int(number_letters)
                