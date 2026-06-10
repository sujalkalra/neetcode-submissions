class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def clean(i,j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                clean(i+1,j)
                clean(i-1,j)
                clean(i,j+1)
                clean(i,j-1)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    clean(r,c)
        return count