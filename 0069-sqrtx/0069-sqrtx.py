class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left = 0 
        right = x
        idx = 0
        mid = (left+right)//2
        while left <= right:
            if mid*mid == x:
                return mid
            elif x < mid*mid :
                right = mid - 1
            else:
                left = mid + 1
                idx = mid
            mid = (left+right)//2
        return idx
