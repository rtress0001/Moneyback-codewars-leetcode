class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        reverse = str(num)[::-1]
        reverse = int(reverse)
        reverse = str(reverse)[::-1]
        return reverse