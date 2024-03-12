class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        reverse = str(num)
        reverse = reverse[::-1]
        reverse = int(reverse)
        reverse = str(reverse)
        return int(reverse[::-1])  == num