class Solution:
    def splitNum(self, num: int) -> int:
        
        #sort the string
        string = sorted(str(num))
        
        #declare varaibles
        num1 = ""
        num2 = ""
        i = 0
        
        #loop though the list filtering between num1 and num2
        for ele in string:
            if i%2==0:
                num1+=ele
            else:
                num2+=ele
            i+=1
        
        return int(num1)+int(num2)
           
        
        
        
       