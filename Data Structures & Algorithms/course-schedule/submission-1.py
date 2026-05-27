class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj graph
        adj = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adj[prereq[0]].append(prereq[1])

        """
        Approach:
        - for every node, run DFS
            - maintain a set of visited to find cycles
            - if cycle true, return false and end
            - if no cycles found, for every node remove its children
                - this is to mark that course as able to be taken
        """

        def _dfs(curr, visited) -> bool:
            # do stuff
            if curr in visited: # cycle hit
                return False

            print(f"visiting {curr}")
            print(f"dependencies: {adj[curr]}")
            
            visited.add(curr)
            
            for next in adj[curr]:
                if not _dfs(next, visited):
                    return False
            
            adj[curr].clear()
            visited.remove(curr)
            
            # print(f"{curr} is good")
            return True
        
        for i in range(numCourses):
            if not _dfs(i, set()):
                return False
        
        return True
        
