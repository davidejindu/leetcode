# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        node = root
        count = 0

        while node or result:
            while node:
                result.append(node)
                node = node.left

            node = result.pop()
            count +=1

            if count == k:
                return node.val

            node = node.right
