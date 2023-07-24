# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # full tree will be stored in BFS (I.E. Level Order)
        full_tree = []

        # deque for storing each level
        queue = collections.deque()
        # start by appending the root node
        queue.append(root)


        # while we still have values in our deque
        while queue:
            # get the len of our queue to know how many nodes we have to progress across on this current level
            level_len = len(queue)

            # level vals to be stored
            level = []

            # iterate through the current level
            for i in range(level_len):
                # keep popping from the left until the entire level has been iterated across
                node = queue.popleft()
                # check if the node is non null before calling its children
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            # if the level contains values append it to our final list
            if level:
                full_tree.append(level)

        return full_tree


