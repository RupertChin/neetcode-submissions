class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Approach:
        - run flood fill (dfs) from every node
        - whenever you start at an unvisited node increment counter
        """

        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()
        def _dfs(curr: int, prev: int):
            nonlocal visited, adj
            if curr in visited:
                return
            visited.add(curr)

            for next_node in adj[curr]:
                _dfs(next_node, curr)
        
        num_components = 0
        for i in range(n):
            if i not in visited:
                num_components += 1
                _dfs(i, -1)
        
        return num_components
