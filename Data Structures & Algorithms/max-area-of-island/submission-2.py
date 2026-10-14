from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        maxArea = 0
        visited = set()
        
        def dfs(r,c):
            if (
                r < 0 or 
                r >= n or 
                c < 0 or 
                c >= m or 
                (r,c) in visited or 
                grid[r][c] == 0):
                return 0

            visited.add((r,c)) 
            area = 1

            area += dfs(r-1,c)
            area += dfs(r+1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)

            return area
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if (i,j) in visited:
                        continue
                    currArea = dfs(i,j)
                    maxArea = max(maxArea, currArea)
                    currArea = 0

        return maxArea

        #go through each row, if we see a 1 then do dfs and each iteration 
        #update the area and then compare currarea with max area

        #return max area