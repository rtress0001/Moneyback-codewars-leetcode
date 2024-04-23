class Solution:
    def sortSentence(self, s: str) -> str:
        #split the strings into list of words
        words = s.split()
        
        words.sort(key = lambda x:  int(x[-1]))
        
        sentence = ''
        for ele in words:
            sentence+=ele[:len(ele)-1] + " "
        return sentence.strip()