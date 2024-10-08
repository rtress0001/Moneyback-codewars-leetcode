class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        current_width = 0 
        
        for ele in s:
            ele_width = widths[ord(ele)-ord('a')]
            
            if current_width + ele_width > 100:
                lines+=1
                current_width=ele_width
            else:
                current_width+=ele_width
                
        return [lines,current_width]