class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        #declare spreate lsts the array into odd and even lsts
        even = []
        odd = []
        lst = []
        
        #create a loop that splits the lst into the odd or even lst
        for i in range(len(nums)):
                            
            #filter lst into odd or even lsts
                if nums[i] % 2 == 0:
                    even.append(nums[i])
                else:
                     odd.append(nums[i])
                       
        #declare seprate pointer for odd and even
        odd_i, even_i = 0,0
        #merge the lsts with match indicies
        for i in range(len(nums)):
            if i % 2 == 0:
                lst.append(even[even_i])
                even_i +=1
            else:
                lst.append(odd[odd_i])
                odd_i +=1
                
                       
        
        #return the new lst
        return lst
        
        
        