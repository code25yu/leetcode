class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        start_pxl = image[sr][sc]
        if start_pxl == color:
            return image

        rows = len(image)
        columns = len(image[0])    
        def dfs(r, c):
            if 0 > r or r >= rows or 0 > c or c >= columns:
                return
            if image[r][c] != start_pxl:
                return
            image[r][c] = color

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        dfs(sr, sc)
        return image