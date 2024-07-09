class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        #creates place to store the elements
        lst = []
        for ele in s:
            if lst and lst[-1] == ele:
                lst.pop()
            else:
                lst.append(ele)
        
        return "".join(lst)
        
        