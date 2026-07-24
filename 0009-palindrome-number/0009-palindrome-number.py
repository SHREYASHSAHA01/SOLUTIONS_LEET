class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        r = 0
        num = str(x)
        left = 0
        right = len(num) - 1
        for i in range(len(num)-1):
            if num[left] != num[right]:
                return False
            left += 1
            right -= 1
        return True