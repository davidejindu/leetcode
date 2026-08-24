# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
so i want a same tree function

then i want to call it on each node in the root
see if it returns True
if it returns True atleast once then we found a subtree

if not subRoot return True

if not root return False

"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(t1,t2):
            if not t1 and not t2:
                return True

            if (t1 and not t2) or (not t1 and t2):
                return False

            if t1.val != t2.val:
                return False

            return sameTree(t1.left,t2.left) and sameTree(t1.right,t2.right)


        def sameSubRoot(root, subRoot):
            if not subRoot:
                return True

            if not root:
                return False

            if sameTree(root,subRoot):
                return True

            return sameSubRoot(root.left,subRoot) or sameSubRoot(root.right,subRoot)


        return sameSubRoot(root,subRoot)


        