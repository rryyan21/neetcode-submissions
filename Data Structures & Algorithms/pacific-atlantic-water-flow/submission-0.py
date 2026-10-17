class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        visited_p = set()
        visited_a = set()
        res = []

        def dfs(r,c,visited):
            if (r,c) in visited:
                return

            visited.add((r,c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if(
                    0 <= nr < n and 
                    0 <= nc < m and
                    (nr, nc) not in visited and
                    heights[r][c] <= heights[nr][nc]
                ):
                    dfs(nr,nc,visited)


        for i in range(n):
            dfs(i,0,visited_p)
            dfs(i,m-1,visited_a)

        for j in range(m):
            dfs(0,j,visited_p)
            dfs(n-1,j,visited_a)

        
        for r,c in visited_p & visited_a:
            res.append((r,c))
            
        return res