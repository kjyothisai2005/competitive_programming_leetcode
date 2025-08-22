class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
    
        r = len(grid)
        c = len(grid[0])
    
        min_row, max_row = float('inf'), float('-inf')
        min_col, max_col = float('inf'), float('-inf')
    
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row,i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
        width = max_col-min_col+1
        height = max_row-min_row+1
        area = width * height
    
        return area