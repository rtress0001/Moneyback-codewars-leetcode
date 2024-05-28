class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        string = ""
        for index in range(1,num+1):
            string = str(index)
            sum_of_digits = 0
            for ele in string:
                sum_of_digits += int(ele)
            if sum_of_digits % 2 == 0:
                count +=1
        return count
            
        