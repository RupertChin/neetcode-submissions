from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Approach: 
        - Run bfs from each rotten fruit
            - Track in 2d arr time taken to rot (or inf)
            - May rot faster from diff banana, keep updating min
        - Check each banana square after for max time taken
        - If banana has inf, then return -1
        """

        time_to_rot = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def bfs(start_row, start_col):
            dq = deque()
            dq.append((start_row, start_col, 0))
            seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
            while len(dq) > 0:
                row, col, t_elapsed = dq.popleft()

                if row < 0 or row >= len(grid):
                    continue
                if col < 0 or col >= len(grid[0]):
                    continue
                if seen[row][col] or grid[row][col] == 0:
                    continue
            
                seen[row][col] = True
                time_to_rot[row][col] = min(time_to_rot[row][col], t_elapsed)

                dq.append((row-1, col, t_elapsed + 1))
                dq.append((row+1, col, t_elapsed + 1))
                dq.append((row, col-1, t_elapsed + 1))
                dq.append((row, col+1, t_elapsed + 1))
        
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 2:
                    bfs(r, c)
        

        print(time_to_rot)
        max_time_to_rot = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    if time_to_rot[row][col] == float('inf'):
                        return -1
                    else:
                        max_time_to_rot = max(max_time_to_rot, time_to_rot[row][col])
        
        return max_time_to_rot


