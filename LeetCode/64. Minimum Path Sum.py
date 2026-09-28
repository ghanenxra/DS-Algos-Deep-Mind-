class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        def dfs(row, col):
            if row==m-1 and col==n-1:
                return grid[row][col]

            if row>=m or col>=n:
                return float("inf")

            down=dfs(row+1, col)
            right=dfs(row, col+1)

            return grid[row][col] + min(down, right)
        return dfs(0,0)