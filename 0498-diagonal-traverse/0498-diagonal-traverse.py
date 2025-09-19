class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        d = {}
        
        for i in range(m):
            for j in range(n):
                if i + j not in d:
                    d[i + j] = []
                d[i + j].append(mat[i][j])
        
        result = []
        for k in range(n + m - 1):
            if k % 2 == 0:
                result.extend(d[k][::-1])
            else:
                result.extend(d[k])
        return result