# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

use the preorder and inorder arrays to construct the binary tree

3,9,20,15,7
  ^ 
9 = root


9,3,15,20,7
  ^
we know that the first value in preorder is the root then we 
know everything till we reach the index of that root in inorder array is on the left of binary tree 

"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return 

        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return root


        