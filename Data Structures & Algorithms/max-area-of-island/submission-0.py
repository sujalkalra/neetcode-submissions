class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def calc(i,j):
            if i in range(0,len(grid)) and j in range(0,len(grid[0])) and grid[i][j] == 1:
                grid[i][j] = 0
                return (1 +
                calc(i+1,j)+
                calc(i-1,j)+
                calc(i,j+1)+
                calc(i,j-1)
                )
            else:
                return 0 
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(res,calc(r,c))
        return res