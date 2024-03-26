def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()
        for ele in s:
            if ele in seen:
                return ele
            else:
                seen.add(ele)
        
            