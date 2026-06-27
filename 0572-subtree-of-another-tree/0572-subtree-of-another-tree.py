# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p,q):
            if not p and not q:
                return True

            if (not p and q) or (p and not q):
                return False

            if p.val != q.val:
                return False

            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)


        def same_subroot(root):
            if not root:
                return False

            if not subRoot:
                return True

            if isSameTree(root,subRoot):
                return True

            return same_subroot(root.left) or same_subroot(root.right)


        return same_subroot(root)

        