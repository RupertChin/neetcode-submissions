# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getKthSmallest(self, root: Optional[TreeNode], count: int, k: int) -> tuple(int, int):
        if not root:
            return (count, None)
        
        # left child first
        count, val = self.getKthSmallest(root.left, count, k)

        count += 1
        # return early if already found
        if val is not None:
            return (count, val)

        # check root node
        if count == k:
            return (count, root.val)
        
        count, val = self.getKthSmallest(root.right, count, k)

        return (count, val)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Approach:
        In order traversal of tree, tracking how many nodes appeared so far
        Done recursively, each function returns tuple(count, kth value)
        """
        return self.getKthSmallest(root, 0, k)[1]

