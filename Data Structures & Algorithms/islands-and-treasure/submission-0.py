class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m,n = len(grid),len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:
            i,j = q.popleft()
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni,nj = i + di , j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] == INF:
                    grid[ni][nj]=grid[i][j]+1
                    q.append((ni,nj))
        
