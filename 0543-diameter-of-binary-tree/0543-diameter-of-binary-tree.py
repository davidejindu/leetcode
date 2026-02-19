# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.largest_diameter = 0
        """

        you want to make a global variable for largest diameter
        the diameter is just the height of left and right child added together
        


        """

        def dfs(node):

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.largest_diameter = max(self.largest_diameter,left + right)


            return 1 + max(left,right)

        dfs(root)
        return self.largest_diameter


        