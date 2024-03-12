def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = ""
        for ele in s:
            if ele.isalnum():
                clean += ele.lower()
        return clean == clean[::-1]