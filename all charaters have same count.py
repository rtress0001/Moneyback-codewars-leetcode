class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        lists = list(s)
        
        freq = lists.count(lists[0])
        
        return all(lists.count(ele) == freq for ele in lists)
            