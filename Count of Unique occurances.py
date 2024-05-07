class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        fequency_count = {}
        for ele in arr:
            fequency_count[ele] = fequency_count.get(ele,0)+1
        return len(fequency_count.values()) == len(set(fequency_count.values()))
      