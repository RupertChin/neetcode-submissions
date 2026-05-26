# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        """
        Approach:
        At each node:
        - recursively call function on each child node
        - take max between sum of returned child node path sum (see note below)
            - func returns max between its 2 child recursive calls and current node val
        - highest possible path in this subtree is max of: 
            - either or sum of left and right child recursive calls
            - current node value
        - compare this to max_path_sum and set if applicable
        """

        def getMaxPathSum(root: Optional[TreeNode]) -> int:
            nonlocal max_path_sum

            if not root:
                return float("-inf")
            
            max_left = getMaxPathSum(root.left)
            max_right = getMaxPathSum(root.right)

            max_path_sum = max(max_path_sum, max_left + root.val, max_right + root.val, max_left + max_right + root.val, root.val)

            cur_path_sum = max(max_left, max_right, 0)
            cur_path_sum += root.val

            return cur_path_sum
        
        getMaxPathSum(root)
        return max_path_sum