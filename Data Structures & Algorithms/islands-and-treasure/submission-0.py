from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #use multisource bfs 
        #before beginning bfs fill the queue with all the places of the treasure chest so that we can do bfs out from there and place the num distances in the grid

        n = len(grid)
        m = len(grid[0])
        queue = deque()
        visited = set()

        def bfs():
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            while queue:    
                r,c = queue.popleft()
                visited.add((r,c))
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 2147483647):
                        grid[nr][nc] = 1 + grid[r][c]
                        queue.append((nr,nc))
                    
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i,j))

        bfs()
