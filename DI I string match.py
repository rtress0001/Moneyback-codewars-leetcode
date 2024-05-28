class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        I = 0
        D = n
        lst = []
        for ele in s:
            if ele == "I":
                lst.append(I)
                I+=1
            else:
                lst.append(D)
                D-=1
        lst.append(I)
        return lst
                
