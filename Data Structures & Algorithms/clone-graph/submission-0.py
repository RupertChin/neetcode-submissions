"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = [None] * 101

        def _cloneGraph(new_node, ref_node) -> None:
            nonlocal visited
            # if visited[val]:
            #     return
            
            print(f"visiting: {new_node.val}")
            visited[new_node.val] = new_node
            print(visited[0:5])

            for neighbor in ref_node.neighbors:
                if not visited[neighbor.val]:
                    copy_node = Node(neighbor.val)
                    new_node.neighbors.append(copy_node)
                    _cloneGraph(copy_node, neighbor)
                else:
                    new_node.neighbors.append(visited[neighbor.val])
            
            return
        
        if not node:
            return None

        start = Node(node.val)
        _cloneGraph(start, node)

        return start
                