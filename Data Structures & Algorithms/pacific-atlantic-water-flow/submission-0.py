class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, ocean):
            ocean.add((i, j))
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and (nx, ny) not in ocean
                    and heights[nx][ny] >= heights[i][j]
                ):
                    dfs(nx, ny, ocean)

        pacific, atlantic = set(), set()
        for j in range(n):
            dfs(0, j, pacific)
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(m - 1, j, atlantic)
        for i in range(m):
            dfs(i, n - 1, atlantic)
        return list(pacific & atlantic)