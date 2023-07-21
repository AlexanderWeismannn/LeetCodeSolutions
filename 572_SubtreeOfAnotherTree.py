# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # if our subtree is Null we can always return True 
        if not subRoot:
            return True

        # if our original tree is empty and our subtree isnt then the answer is always false
        if not root and subRoot:
            return False

        # if we know that our subtree is a subtree of our root we return true
        if self.sameTree(root,subRoot):
            return True

        # otherwise we call our method again having gone down the left and right path of the root. We only need one of these
        # to be right for our answer to be true
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    # # same tree helper method
    def sameTree(self,root,subRoot):


        # they are both empty trees
        if not root and not subRoot:
            return True

        # if they are the same we need to backtrack up and keep comparing
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right)
        
        # if at any point the values do not match then the False will propagate back up the tree and our
        # final answer will be false for the sameTree     
        return False

 
