# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        can do iterative inorder
        so stack would have 1 increment count
        if count == k return node


        """

        stack = []
        result = []
        node = root
        count = 0

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            count +=1
            node = stack.pop()
            result.append(node.val)
            node = node.right
            if count == k:
                return result[-1]