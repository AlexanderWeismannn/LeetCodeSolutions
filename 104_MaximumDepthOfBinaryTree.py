# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # This solution will implement recursion

        # We have passed the leaf node and 
        if root == None:
            return 0

        # we recursively call the left and right nodes of the tree
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)

        # we take the maximum value of the left and right 
        return max(left,right)

        
