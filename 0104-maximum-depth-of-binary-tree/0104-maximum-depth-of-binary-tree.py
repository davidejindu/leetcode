# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

so you need to dfs down to the bottom and start counting from bottom to top

if the node is none you return 0

you want to return the height of the max left or right + 1

"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            return 1 + max(left,right)

        return dfs(root)
        