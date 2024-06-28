class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
         #a list of averages
        average_lst = []
        
        #iterate over the list as it decreases in size
        while len(nums)>1:
            #extablish a max and min variables:
            neg_min = float("inf")
            post_max = float("-inf")
            #find the max and min of thet list
            neg_min = min(nums)
            post_max = max(nums)
            #remove select elements from a list
            nums.remove(neg_min)
            nums.remove(post_max)
            #append averages to lst
            average_lst.append((neg_min+post_max)/2)
            
            
        #return the new list
        return len(set(average_lst))