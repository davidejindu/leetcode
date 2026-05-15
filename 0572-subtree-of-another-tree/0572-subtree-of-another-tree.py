# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        create a method that checks if tree is same
        

        make subroot method that runs that method on each root on subtree
        if there is no subroot automatically true if no root then its false
        


        """

        def sameTree(r1, r2):
            if not r1 and not r2:
                return True

            if (not r1 and r2) or (r1 and not r2):
                return False

            if r1.val != r2.val:
                return False

            return sameTree(r1.right,r2.right) and sameTree(r1.left,r2.left)



        def is_subtree(root):
            if not subRoot:
                return True

            if not root:
                return False

            if sameTree(root,subRoot):
                return True

            return is_subtree(root.left) or is_subtree(root.right)

        return is_subtree(root)