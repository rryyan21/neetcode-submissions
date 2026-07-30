class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        bestArea = 0
        currArea = 0

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            count = 1
            grid[i][j] = 0
            count += dfs(i+1,j)
            count += dfs(i-1,j)
            count += dfs(i,j+1)
            count += dfs(i,j-1)
            return count
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    bestArea = max(bestArea, area)
        return bestArea 