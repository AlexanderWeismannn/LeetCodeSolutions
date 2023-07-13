# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # This problem utilizes recursion

        # first we have our catch case for when we stop recusively calling
        # We have reached the end of our tree
        if root == None:
            return

        # Here we invert the sub-trees
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # We now call the function again with the left and right pointers as the new root node
        # these will eventually reach the catcher case and stop being called.
        self.invertTree(root.left)
        self.invertTree(root.right)

        # we can then return the root and the full inverted tree
        return root

        
