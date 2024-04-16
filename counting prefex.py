class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        len_pre = len(pref)
        count = 0
        for ele in words:
            if ele[:len_pre] == pref:
                count += 1
        return count