class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for index in range(1,n+1):
            for jndex in range(1,n+1):
                for kndex in range(max(index,jndex),n+1):
                    if index * index + jndex*jndex == kndex*kndex:
                        count+=1
        return count