class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        def dfs(row, col):
            if row==len(triangle):
                return 0

            left=dfs(row+1, col)
            right=dfs(row+1, col+1)

            return triangle[row][col]+min(left, right)
        return dfs(0,0)