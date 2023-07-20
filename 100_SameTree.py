# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #base case we are at the root nodes
        if not p and not q:
            return True

        # one of the vals doesnt exist or they are not the same so not 
        # an exact copy
        if (not p or not q) or (p.val != q.val):
            return False

        # we compare each left and right node, making sure as we
        # backtrack up we can examine the results. Everything must
        # match by the end to return True otherwise the result will be false
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))


