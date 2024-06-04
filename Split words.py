class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        split_words=[]
        for ele in words:
            spilt_check = ele.split(separator)
            for ele1 in spilt_check:
                if ele1!="":
                    split_words.append(ele1)
        return split_words
