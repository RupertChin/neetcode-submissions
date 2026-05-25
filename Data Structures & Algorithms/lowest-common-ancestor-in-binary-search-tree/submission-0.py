# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Approach:
        - is a BST, LCA will always be first value found between p and q
        """
        # get low, high values
        low = None
        high = None
        if p.val < q.val:
            low = p
            high = q
        else:
            low = q
            high = p
        
        while not (low.val <= root.val and root.val <= high.val):
            if root.val < low.val: # both p, q greater
                root = root.right
            else: # root > high both p, q lesser
                root = root.left
        
        return root
