class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        #candy types eaten
        eaten = []
        
        #number of candies to eat
        n = len(candyType)//2
        
        #find the unique elements of the system
        unique = len(set(candyType))
        
        #return the minimum between the two
        return min(unique,n)
        
        
        
        
        