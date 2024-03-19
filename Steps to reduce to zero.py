def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while num > 0:
            if num%2==0:
                count+=1
                num = num/2
            else:
                count+=1
                num-=1
        return count
                
            