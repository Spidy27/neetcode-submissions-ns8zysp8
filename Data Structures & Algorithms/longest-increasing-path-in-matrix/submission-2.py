class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]

            max_len = 1
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1+ dfs(nr,nc))

            dp[r][c] = max_len
            return max_len

        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))        
        return res