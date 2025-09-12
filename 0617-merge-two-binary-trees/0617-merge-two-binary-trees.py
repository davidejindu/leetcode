# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def sumTrees(self,root1,root2):
           
            if root1 == None and root2 == None:
                return None
            if root1 == None and root2:
                return root2
            if root2 == None and root1:
                return root1
            
            if root1 and root2:
                root1.val = root1.val + root2.val

            
            root1.right = self.sumTrees(root1.right, root2.right)
            root1.left = self.sumTrees(root1.left, root2.left)

            return root1


            
                
            
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.sumTrees(root1,root2)
        