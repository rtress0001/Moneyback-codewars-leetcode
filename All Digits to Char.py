    def replaceDigits(self, s: str) -> str:
        replace = ""
        for i in range(len(s)):
            if i % 2 == 1:
                replace += chr(ord(s[i - 1]) + int(s[i]))
            else:
                replace += s[i]
        return replace