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
        stack_p = deque()
        stack_q = deque()
        stack_p.append(p)
        stack_q.append(q)
        while stack_p and stack_q:
            cur_p = stack_p.pop()
            cur_q = stack_q.pop()

            if not cur_p and not cur_q:
                continue
            elif not cur_p or not cur_q:
                return False

            if cur_p.val != cur_q.val:
                return False
            
            stack_p.append(cur_p.left)
            stack_q.append(cur_q.left)
            stack_p.append(cur_p.right)
            stack_q.append(cur_q.right)
        
        return True
