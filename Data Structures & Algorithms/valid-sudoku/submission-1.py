class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue 

                correct_grid = (i//3) * 3 + (j//3)

                if val in rows[i] or val in cols[j] or val in grid[correct_grid]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                grid[correct_grid].add(val)
        return True



                