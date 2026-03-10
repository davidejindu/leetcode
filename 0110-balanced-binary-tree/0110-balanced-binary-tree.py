# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height_diff = 0

        def height(root):
            if not root: 
                return 0

            leftHeight = height(root.left)
            rightHeight = height(root.right)

            self.height_diff = max(self.height_diff,abs(rightHeight - leftHeight))

            return 1 + max(leftHeight,rightHeight)

    
        height(root)
        if self.height_diff > 1:
            return False
        else:
            return True



        