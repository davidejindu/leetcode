# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""


valid bst if the left max val is root and min value is float('inf')
valid bst if the right min value is the root and max value is float('inf')

so you want a dfs

if root.left >= max return False

if root.right <= min return True

if node is none return True

"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, minn, maxx):
            if not node:
                return True

            if node.val <= minn or node.val >= maxx:
                return False

            return (dfs(node.left,minn,node.val)
            and dfs(node.right,node.val,maxx))


        return dfs(root, float('-inf'), float('inf'))


        