from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        even_nums = []
        for num in nums:
            if num%2==0:
                even_nums.append(num)
                
        if even_nums == []:
            return -1
        
        
        counter_dict = Counter(even_nums)
        max_key = max(counter_dict.values())
        
        candidates = []
        for key, value in counter_dict.items():
            if value == max_key:
                candidates.append(key)

     
        return min(candidates)
        
            
        