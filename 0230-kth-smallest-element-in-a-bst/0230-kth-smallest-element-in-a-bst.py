# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
stack and heap
when heap == len(k) return heap[0]

k = 1
i dont even need a heap since its inorder traversal and a bst so just an array and return
last index when len == k

"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result, stack = [], []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.val)

            if len(result) == k:
                return result[-1]

            node = node.right
        