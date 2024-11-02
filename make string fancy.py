class Solution:
    def makeFancyString(self, s: str) -> str:
        ret = []
        for ele in s:
            if len(ret) >= 2 and ret[-1] == ele and ret[-2] == ele:
                continue
            ret.append(ele)
        
        return "".join(ret)
                