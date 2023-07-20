# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def dfs(root):

            # base case
            if not root:
                return 0

            # DFS is performed here
            left = dfs(root.left)
            right = dfs(root.right)

            # compare current dimater with max (i.e. self.diameter value)
            self.diameter = max(left+right,self.diameter)
            # return the longest subtree, this value will get pushed up the tree and be the new left / right value that is compared 
            return max(left,right)+1

        dfs(root)
        return self.diameter


