class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = []
        for i in range(m):
            res = []
            for j in range(n):
                if i == 0 or j == 0:
                    res.append(1)
                else:
                    res.append(0)
            grid.append(res)

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]