class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        max_num = ""
        

        for i in range(len(num) - 2):
            sub_string = num[i:i+3]
            
            
            if sub_string[0] == sub_string[1] == sub_string[2]:
                
                if sub_string > max_num:
                    max_num = sub_string
        
        return max_num
            
            