class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths = [[0] * n for _ in range(m)]

        for i in range(m):
            num_paths[i][n-1] = 1
        for i in range(n):
            num_paths[m-1][i] = 1
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                num_paths[i][j] = num_paths[i+1][j] + num_paths[i][j+1]
        
        return num_paths[0][0]
