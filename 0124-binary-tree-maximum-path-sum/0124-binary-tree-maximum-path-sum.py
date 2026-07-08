# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
return max path of binary tree

want to dfs and return node.val and max of node.right and node.left

set the maxx equal to the max of left and right + node.val


"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxx = 0

        def dfs(node):
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            leftMax= max(leftMax, 0)
            rightMax = max(rightMax, 0)


            self.maxx = max(self.maxx, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)

        dfs(root)
        return self.maxx