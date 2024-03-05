class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maxalt = 0
        start = 0
        for change in gain:
            start += change
            maxalt = max(maxalt,start)
        return maxalt