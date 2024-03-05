class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        for i in range(len(string)):
            if string[i] == '6':
                return int(string[:i] + '9' + string[i+1:])
        return int(string)
