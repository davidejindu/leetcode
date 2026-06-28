# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
check if left node is less than the current node 
and 

check if right node is greater than current node but isnt less than root node

need a bounds constraint

when going left it has a maximum bound of anything less than current node and mas
an unlimited minimum bound

when going right it has a minimum bound of the root and a unlimited maximum bound

def dfs(node, maxbound, minbound):
    if not node:
        return True

    if node.val > maxbound or node.val < minbound:
        return False




"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, maxbound, minbound):
            if not node:
                return True

            if node.val >= maxbound or node.val <= minbound:
                return False

            return (dfs(node.left,node.val,minbound)
            and dfs(node.right,maxbound,node.val))


        return dfs(root,float('inf'), float('-inf'))



        