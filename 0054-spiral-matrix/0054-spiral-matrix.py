class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        l, r = 0, len(matrix[0]) - 1 # n
        t, b = 0, len(matrix) - 1    # m 
        res = []
        while l <= r and t <= b:
            # 1. left > right : 고정행:top
            for j in range(l, r + 1):
                res.append(matrix[t][j])
            t+=1
            # 2. top > bottom : 고정열:right
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r-=1
            # 3. right > left: 고정행:bottom
            if t <= b:
                for j in range(r, l - 1, -1):
                    res.append(matrix[b][j])
                b-=1
            # 4. bottom > top: 고정열:left
            if l <= r:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l+=1
        return res
            