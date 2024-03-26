def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        halfpoint = len(s)//2
        righthalfcnt = 0
        lefthalfcnt = 0
        vowels = "aeiouAEIOU"
        for ele in s[:halfpoint]:
            if ele in vowels:
                righthalfcnt +=1
        for ele in s[halfpoint:]:
            if ele in vowels:
                    lefthalfcnt +=1
        return righthalfcnt == lefthalfcnt
        