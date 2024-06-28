class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        #construct a postive list
        neg_arr = []
        #construct a negative lst
        pos_arr = []
                
        #loop though the lst splitting them into postive and negavtives
        for num in nums:
            #append if postive
            if num>0:
                pos_arr.append(num)
            elif num<0:
                neg_arr.append(num)
                                
        
        #return the longest list length
        if len(pos_arr)>len(neg_arr):
            return len(pos_arr)
        else:
            return len(neg_arr)
        