class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        #declare a lst to sepeate into
        even = []        
        odd = []
        lst = []
        #sperate indices into odd lst and even lst
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
            
        #sort the new lsts by the order of them.
        odd.sort(reverse=True)
        even.sort(reverse=False)
         
        #declare even and odd indices
        even_index, odd_index = 0, 0
        #loop though the list to select for odd and even indicies
        for i in range(len(nums)):
            if i % 2 == 0:
                lst.append(even[even_index])
                even_index+=1
            else:
                lst.append(odd[odd_index])
                odd_index+=1
        #return the sorted lst        
        return lst