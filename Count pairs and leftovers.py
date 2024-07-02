from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        #make a dictionary for that cotains frequency of each value
        count_freq = Counter(nums)
        
        #declare variables to be used in the loop
        num_pairs = 0
        num_leftovers = 0
        
        #create a loop that loops over the values of the pairs
        for value in count_freq.values():
            num_pairs += value//2
            num_leftovers += value%2
            
        #return the values from the loop
        return [num_pairs,num_leftovers]
            
        
        