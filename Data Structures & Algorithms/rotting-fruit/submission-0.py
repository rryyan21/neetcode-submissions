from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #keep count of how mant fruits there are
        #store first rotten fruit into queue
        #run bfs on the rotten fruit and increment time count per iterat
        #if bfs ends and fruits is not 0 return -1 otherwise return time


        #or should i use dfs 
        #pretty sure bfs since it could be in the middle and spread outward per minute so dfs wouldnt work 
        fresh = 0
        time = 0
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        directions = [(1,0),(-1,0), (0,1), (0,-1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))


        while queue and fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
            time += 1

        if fresh > 0:
            return -1
        else:
            return time

        