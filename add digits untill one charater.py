class Solution:
    def addDigits(self, num: int) -> int:
        string = ""
        while len(str(num)) > 1:
            string = str(num)
            sum_of_digits = 0
            for ele in string:
                sum_of_digits += int(ele)
            num = sum_of_digits
        return num
            
            
            