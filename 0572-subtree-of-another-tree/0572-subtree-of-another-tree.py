# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same_tree(t1,t2):
            if not t1 and not t2:
                return True

            if (t1 and not t2) or (not t1 and t2):
                return False

            if t1.val != t2.val:
                return False

            return same_tree(t1.left,t2.left) and same_tree(t1.right,t2.right)


        def same_subTree(root,subRoot):
            if not subRoot:
                return True

            if not root:
                return False

            if same_tree(root, subRoot):
                return True


            return same_subTree(root.left,subRoot) or same_subTree(root.right,subRoot)


        return same_subTree(root,subRoot)
        