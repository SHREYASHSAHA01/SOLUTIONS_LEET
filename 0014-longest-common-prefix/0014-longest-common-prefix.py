class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        i = 0
        while i < len(strs[-1]) and i < len(strs[0]) and strs[-1][i] == strs[0][i]:
            i += 1
        return strs[0][:i]