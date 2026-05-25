# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkValidBST(self, root: TreeNode) -> tuple(bool, int, int):
        if not root:
            return (True, 0, 0)
        
        cur_min = None
        cur_max = None
        if root.left:
            res, child_min, child_max = self.checkValidBST(root.left)
            if not res:
                return (False, 0, 0)
            if child_max >= root.val:
                return (False, 0, 0)
            cur_min = child_min
        if root.right:
            res, child_min, child_max = self.checkValidBST(root.right)
            if not res:
                return (False, 0, 0)
            if child_min <= root.val:
                return (False, 0, 0)
            cur_max = child_max
        
        if cur_min is None:
            cur_min = root.val
        if cur_max is None:
            cur_max = root.val
        
        return (True, cur_min, cur_max)
            


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Approach:
        - recursion, get max of left, min of right per node, must be valid"
        - each recursive call returns a tuple containing the range of that subtree
        """
        return self.checkValidBST(root)[0]
        