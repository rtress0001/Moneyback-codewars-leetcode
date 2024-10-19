class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s2 = []
            for i in range(0,len(s),k):
                sgroup = s[i:i+k]
                digit_sum = 0
                for ele in sgroup:
                    digit_sum += int(ele)
                s2.append(str(digit_sum))
            s = "".join(s2)
            
        return s
            