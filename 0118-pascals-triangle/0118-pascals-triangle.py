class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        lis = []
        for i in range(numRows):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = lis[i-1][j-1]+ lis[i-1][j]
            lis.append(row)   
        return lis
