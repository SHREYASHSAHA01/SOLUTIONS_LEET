class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lis = []
        for i in range(rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1,i):
                row[j] = lis[i-1][j-1] + lis[i-1][j]
            lis.append(row)
        return lis[rowIndex]
        