class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
            
        neg = (dividend < 0) ^ (divisor < 0)
        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        final_count = 0
        
        while abs_divisor <= abs_dividend:
            temp_divisor = abs_divisor
            temp_count = 1
            
            while (temp_divisor << 1) <= abs_dividend:
                temp_divisor <<= 1
                temp_count <<= 1
                
            abs_dividend -= temp_divisor
            final_count += temp_count
            
        return -final_count if neg else final_count