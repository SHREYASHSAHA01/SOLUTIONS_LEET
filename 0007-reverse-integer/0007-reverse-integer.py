class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0  :
            return 0
        a = []
        sign = False
        if x < 0:
            x = -x
            sign = True
        while x:
            r = x%10
            a.append(str(r))
            x = x//10
        x = int("".join(a))
        if (x < -(2**31)) or x > (2**31)-1 :
            return 0
        if sign:
            return -x
        return x
        

