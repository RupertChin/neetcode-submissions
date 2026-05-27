class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        A graph is a tree if:
        - all nodes are reachable from others
        - no cycles are present

        Approach 1:
        - build graph
        - run DFS, keep track of previous node to ensure erroneous 
        cycles aren't found
        - ensure all nodes have been visited, no cycles found

        Approach 2:
        - Create sets of nodes, starting with one node per set
        - For each edge, join the sets each node is in (if different)
        - should only be 1 set at the end
        - to detect cycles: there should only be n - 1 edges

        Approach 1 has better time complexity, 
        can easily detect cycles
        """
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()
        def _dfs(curr: int, prev: int) -> bool:
            nonlocal adj, visited
            if curr in visited:
                return False
            visited.add(curr)

            for next in adj[curr]:
                if next != prev and not _dfs(next, curr):
                    return False

            return True
        
        if not _dfs(0, -1):
            return False
        return len(visited) == n
        
            