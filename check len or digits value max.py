class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        #store the maxiumun
        max_value = 0
        
        #loop though the list filtering for string or digits
        for ele in strs:
            if ele.isdigit():
                max_value = max(int(ele),max_value)
            else:
                max_value = max(len(ele),max_value)
        return max_value