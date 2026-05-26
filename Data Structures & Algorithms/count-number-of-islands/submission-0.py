class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def floodfill(row: int, col: int) -> None:
            nonlocal grid

            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] != '1':
                return
            
            grid[row][col] = '*'
            floodfill(row+1, col)
            floodfill(row-1, col)
            floodfill(row, col+1)
            floodfill(row, col-1)
        
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    floodfill(row, col)
                    num_islands += 1
        
        return num_islands