# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       
        def dfs(root):
        
            # base case, we are at a node with no children
            # It IS balanced and has a height of 0
            if not root:
                return [True,0]

            # recursively call dfs
            left = dfs(root.left)
            right = dfs(root.right)

            # determine if the tree is balanced so far. This is true if left and right are both balanced, and the difference between left and right is <= 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # we the get the height of the current subtree by taking the max of left and right + 1
            height = max(left[1],right[1])+1
            # backtracking up the tree, returning whether the current node is balanced and its height
            return [balanced,height]

        # def return a list [balanced,height], we only care about the boolean value T/F
        return dfs(root)[0]
        



