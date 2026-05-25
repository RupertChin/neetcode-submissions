# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach:
        - BFS traversal to get every node and its depth
        - store as (value, depth) in a queue
        - build result array, appending new arr per new depth found
        """
        queue = deque()
        queue.append((root, 1))
        nodes = deque()
        while queue:
            curr = queue.popleft()
            if not curr[0]:
                continue
            
            nodes.append(curr)
            queue.append((curr[0].left, curr[1]+1))
            queue.append((curr[0].right, curr[1]+1))
        
        res = []
        while nodes:
            node, depth = nodes.popleft()
            if depth > len(res):
                res.append([node.val])
            else:
                res[depth-1].append(node.val)
        
        return res
