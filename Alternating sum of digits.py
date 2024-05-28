class Solution:
    def alternateDigitSum(self, n: int) -> int:
        count = 0
        sum_of_digits = 0
        string = str(n)
        for ele in string:
            if count % 2 == 1:
                sum_of_digits -= int(ele)
            else:
                sum_of_digits += int(ele)
            count+=1
        return sum_of_digits
        