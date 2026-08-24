# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
want to get max path sum

need to return the max of left, right + node.val

then need to store max in global variable

the max global variable will be node.val + leftMax + rightMax

if not node:
    return 0



"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxx = root.val

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            leftMax = max(left,0)
            rightMax = max(right,0)

            self.maxx = max(self.maxx,node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)

        dfs(root)

        return self.maxx