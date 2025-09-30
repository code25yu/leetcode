from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        # 행과 열 개수 구하기
        rows, cols = len(grid), len(grid[0])
        
        # 방문 여부를 기록할 2차원 배열 (처음엔 모두 false)
        visited = [[False]*cols for _ in range(rows)]
        
        # 섬 개수 카운트 변수
        islands = 0
        
        # 4방향 탐색을 위한 좌표 변화 (상, 하, 좌, 우)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS 함수: (sr, sc)에서 시작해 연결된 모든 '1'을 탐색
        def bfs(sr, sc):
            q = deque()
            
            # 시작 좌표를 큐에 넣음
            q.append((sr, sc))
            # 방문 처리
            visited[sr][sc] = True

            # 큐가 빌 때까지 반복
            while q:
                r, c = q.popleft() # 큐에서 현재 좌표 꺼내기 
                
                # 4방향 이웃 탐색
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc  
                    
                    # 1. 그리드 범위 안에 있고 
                    # 2. 아직 방문하지 않았으며
                    # 3. 땅('1')일 때 
                    if 0 <= nr < rows and 0 <= nc < cols \
                       and not visited[nr][nc] \
                       and grid[nr][nc] == '1':
                        visited[nr][nc] = True
                        q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    bfs(r, c)
                    islands += 1

        return islands