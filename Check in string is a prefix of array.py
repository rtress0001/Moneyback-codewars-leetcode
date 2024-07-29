class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        #empty string
        con = ""
        
        for word in words:
            con+=word
            if con == s:
                return True
            if len(con) > len(s):
                return False
        
        