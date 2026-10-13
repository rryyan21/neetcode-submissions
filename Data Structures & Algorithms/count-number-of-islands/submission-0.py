from collections import deque 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        visited = set()
        islands = 0

        def bfs(r,c):
            directions = [(1,0), (-1,0), (0,-1), (0,1)]
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                r,c = queue.popleft()
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if not 0 <= nr <= n-1 or not 0 <= nc <= m-1:
                        continue

                    if grid[nr][nc] == '0':
                        continue

                    if (nr,nc) in visited:
                        continue

                    queue.append((nr,nc))
                    visited.add((nr,nc))
                    
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j] == '1':
                    islands += 1
                    bfs(i,j)

                
        return islands

        
