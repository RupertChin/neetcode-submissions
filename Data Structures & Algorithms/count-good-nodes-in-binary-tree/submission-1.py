# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findGoodNodes(self, root: TreeNode, max_val: int) -> int:
        # check if current node is good
        num_good_nodes = 1 if root.val >= max_val else 0

        max_val = max(max_val, root.val)

        if root.left:
            num_good_nodes += self.findGoodNodes(root.left, max_val)
        if root.right:
            num_good_nodes += self.findGoodNodes(root.right, max_val)
        
        return num_good_nodes

    def goodNodes(self, root: TreeNode) -> int:
        """
        Approach:
        - recursion, counting num good from left and right child
        - tracking max node value encountered in current path
        - need to check None at recursion call instead of start
            - to determine if current node is check as good or not
        """
        return self.findGoodNodes(root, -101)