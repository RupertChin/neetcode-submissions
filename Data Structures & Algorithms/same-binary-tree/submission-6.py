# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        # # recursive approach, DFS
        # if not p and not q:
        #     return True
        # elif not p or not q:
        #     return False
        
        # if p.val != q.val:
        #     return False

        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # iterative approach, DFS with stack
        stack = deque()
        stack.append(p)
        stack.append(q)
        while stack:
            cur_p = stack.pop()
            cur_q = stack.pop()

            if not cur_p and not cur_q:
                continue
            elif not cur_p or not cur_q:
                return False

            if cur_p.val != cur_q.val:
                return False
            
            stack.append(cur_p.left)
            stack.append(cur_q.left)
            stack.append(cur_p.right)
            stack.append(cur_q.right)
        
        return True
