class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        cum_sum = []
        count = 0
        for ele in operations:
            if ele == "+":
                cum_sum.append(cum_sum[-2]+cum_sum[-1])
            elif ele == "C":
                cum_sum.pop()
            elif ele == "D":
                cum_sum.append(cum_sum[-1]*2)
            else:
                cum_sum.append(int(ele))
            count+=1
        return sum(cum_sum)
                