class Solution(object):
    def plusOne(self, digits):
        num = digits[0]
        i = 1
        while  i < len(digits):
            num = 10*num + digits[i]
            i += 1
        num += 1
        new_lis = []
        while num:
            r  = num%10 
            new_lis.append(r)
            num //= 10
        new_lis.reverse()
        return new_lis

        
        