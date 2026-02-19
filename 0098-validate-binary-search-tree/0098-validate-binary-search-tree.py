# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        """

        start from root

        if root.left and root.left.val > root:
            return false

        if root.right and root.right.value >:
            return false

        maybe make global right nodes list and global left nodes list
        if its less than any of the nodes in the list 

        """

        def valid_BST(node,minn,maxx):
            if node is None:
                return True

            
            if node.val >= maxx or node.val <= minn:
                return False

            return valid_BST(node.left, minn, node.val) and valid_BST(node.right, node.val, maxx)


        return valid_BST(root,float('-inf'), float('inf'))

     
        
            
        