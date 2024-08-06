class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        #sort the arr
        arr.sort()
        
        #declare a trail
        trail = arr[0]
        
        #declare a minimum 
        min_num = float('inf')
        
        #loop though the 
        for num in arr[1:]:
            #make a absoulte difference
            if abs(num - trail) < min_num:
                min_num = abs(num-trail)
            
            trail = num
        
        #loop though the list to find all entries with the differce
        lst = []
        trail = arr[0]
        for ele in arr[1:]:
            if abs(ele-trail) == min_num:
                lst.append([trail,ele])
            trail = ele
        return lst
            
            