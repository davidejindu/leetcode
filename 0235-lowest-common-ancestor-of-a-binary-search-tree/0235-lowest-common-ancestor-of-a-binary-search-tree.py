# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
if root.val > p.val and root.val > q.val move root to the right
elif root.val < p.val and root.val < q.val move root to the left
else return root.val

"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left

            elif root.val < p.val and root.val < q.val:
                root = root.right

            else:
                return root

        return None