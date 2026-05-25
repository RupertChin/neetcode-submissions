# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # recursive approach, DFS
        # if not root:
        #     return 0
        
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # iterative approach, DFS with a stack
        if not root: 
            return 0
        
        max_depth = 0
        stack = deque()
        stack.append((root, 1))
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth
