# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

        so the root is always first index of preorder

        so create tree where it starts root with preorder[0]

        then we know everything to left of 3 in inorder is left subtree
        everything to right of 3 in inorder is right

        thus we should get index of preorder[0]

        then recursve the root.left to make sure that it only captures left of it
        then recurve the root.right to make sure that it only caputreus left of it
        
        
        """

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root