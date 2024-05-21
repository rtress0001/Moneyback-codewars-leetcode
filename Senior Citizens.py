class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        #start the count
        count = 0
        #loop though the list
        for ele in details:
            #filter the list for age
            if int(ele[11])*10 + int(ele[12]) > 60:
                count +=1
        return count
            