from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")
        words = paragraph.split()
        banned_set = set(banned)
        count_words = Counter(word for word in words if word not in banned_set)
        return max(count_words, key=count_words.get)