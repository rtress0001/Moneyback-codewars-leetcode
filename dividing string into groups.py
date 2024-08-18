class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        #storage place for divisions
        divide_lst = []
        
        #tempory string for dividing:
        string = ""
        
        #determine if fill is nessary
        fill_x = (k - len(s) % k) % k
        s+=fill*fill_x
        
        #loop though the lst
        i = 0
        
        for ele in s:
            if len(string) == k:
                divide_lst.append(string)
                string=""
            string+=ele
            i+=1
        #fix last code
        divide_lst.append(string)
                    
        return divide_lst
        
        
       