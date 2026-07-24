class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        num = 0
        for i in range(n):
            num = a + b
            a = b
            b = num
        return num            