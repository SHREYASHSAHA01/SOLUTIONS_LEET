class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        val = 0
        max_val = 0
        while left < right:
            val = min(height[left],height[right])*(right - left)
            max_val = max(max_val,val)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_val