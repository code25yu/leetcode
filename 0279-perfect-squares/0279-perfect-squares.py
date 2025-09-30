from collections import deque

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        
        # BFS
        q = deque([n])
        visited = set([n])
        level = 0
        
        
        while q: # q가 빌 때까지 반복
            level += 1
            for _ in range(len(q)): # q의 개수 만큼 반복 
                curr = q.popleft()
                for sq in squares: # 1, 2, 4, 9 ...
                    nxt = curr - sq
                    if nxt == 0:
                        return level
                    if nxt > 0 and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

        return level