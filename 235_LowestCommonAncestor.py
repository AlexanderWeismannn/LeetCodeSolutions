# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # start at the root node
        current = root

        #loop through our tree
        while current:

            # go left if both vals are smaller
            if p.val < current.val and q.val < current.val:
                current = current.left
            # go right if both vals are bigger
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # p < c.val and q > c.val (otherwise we have found our LCA)
            else:
                return current




        