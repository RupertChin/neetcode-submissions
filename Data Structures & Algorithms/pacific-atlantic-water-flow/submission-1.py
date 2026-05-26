class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Approach 1:
        - dp? iterating through every square twice, forward and backward
        - forward pass for pacific, backward pass for atlantic
            - edges = True, heights greater than squares with True is True
        - pick all squares that have both
        problem: only get paths that go up/left or down/right respectively
        - solution: 2 passes per ocean? no that's not enough...

        Approach 2: 
        - run DFS or BFS, starting from each of the edges
        - Start as None, mark True, False as reachable, visited. 
        """

        def _dfs(i: int, j: int, visited: Set[bool], prev_height) -> None:
            nonlocal heights

            if i < 0 or i >= len(heights):
                return
            if j < 0 or j >= len(heights[0]):
                return
            if (i, j) in visited:
                return
            if prev_height > heights[i][j]:
                return

            print(f"visiting ({i}, {j})")

            visited.add((i, j))
            _dfs(i+1, j, visited, heights[i][j])
            _dfs(i-1, j, visited, heights[i][j])
            _dfs(i, j+1, visited, heights[i][j])
            _dfs(i, j-1, visited, heights[i][j])
            
            # for each dir, if height less than current then visit

        pacific = set()
        atlantic = set()
        
        for i in range(len(heights)):
            _dfs(i, 0, pacific, -1)
            _dfs(i, len(heights[0])-1, atlantic, -1)
        for i in range(len(heights[0])):
            _dfs(0, i, pacific, -1)
            _dfs(len(heights)-1, i, atlantic, -1)
        
        print(pacific)
        print(atlantic)
        return list(pacific & atlantic)


        