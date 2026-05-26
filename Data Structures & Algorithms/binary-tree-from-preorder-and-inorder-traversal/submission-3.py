# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Approach:
        - use preorder for insertion order of nodes, starting from root
        - use inorder to determine if the next node is left or right of current node
            - or if need to return to higher level node to continue
        """
        inorder_pos = {val: i for i, val, in enumerate(inorder)}
        pre_ind = 0 # starts at node after root

        def buildTreeRec(root, left, right) -> None: # left, right is the range of possible nodes
            nonlocal preorder, inorder_pos, pre_ind
            
            pre_ind += 1
            if pre_ind >= len(preorder):
                return

            cur_val = preorder[pre_ind]

            if inorder_pos[cur_val] > left and inorder_pos[cur_val] < inorder_pos[root.val]:
                root.left = TreeNode(cur_val)
                buildTreeRec(root.left, left, inorder_pos[root.val])
            
            if pre_ind >= len(preorder):
                return
            cur_val = preorder[pre_ind]
            
            if inorder_pos[cur_val] < right and inorder_pos[cur_val] > inorder_pos[root.val]:
                root.right = TreeNode(cur_val)
                buildTreeRec(root.right, inorder_pos[root.val], right)
            
            return
        
        root = TreeNode(preorder[0])
        buildTreeRec(root, -1, len(preorder))

        return root
            
