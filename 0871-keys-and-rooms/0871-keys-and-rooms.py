from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
#         # 1. Orginal Version(DFS)
#         if not rooms:
#             return True

#         visited = [False] * len(rooms)
#         def dfs(i):
#             if i < 0 or i >= len(rooms) or visited[i] == True:
#                 return
#             visited[i] = True
#             for key in rooms[i]:
#                 dfs(key)
#         dfs(0)
#         return not False in visited
    
#         # 2. Improved Version
#         if not rooms:
#             return True

#         visited = [False] * len(rooms)
#         def dfs(i):
#             if visited[i]:
#                 return
#             visited[i] = True
#             for key in rooms[i]:
#                 dfs(key)
#         dfs(0)
#         return all(visited)
    
        # 3. BFS Code
        """
        DFS로도 충분하지만, BFS로 구현하면 큐를 사용해 재귀 깊이 초과 위험 없이도 탐색 가능.
        재귀 깊이가 n=1000 정도면 문제 없지만, BFS는 더 안전하다.
        """
        visited = [False] * len(rooms)
        queue = deque([0])
        visited[0] = True
        
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)
        
        return all(visited)
