class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n3 = nums1 + nums2
        n3.sort()
        if len(n3) % 2 == 0:
            return  (n3[len(n3)//2] + n3[len(n3)//2 - 1]) / 2.0
        else :
            return float(n3[len(n3)//2])