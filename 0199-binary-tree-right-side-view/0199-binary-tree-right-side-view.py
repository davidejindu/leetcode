# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

so we always see the root so thats part of the result

we only want the rightmost

so we can append the rightmost to the queue first
and after the first loop we pop the rest of the queue but make sure we add it children

    1
2       3
  5         4

result = [1,3,4]
queue = []


"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            for i in range(len(queue)):
                if i == 0:
                    node = queue.popleft()
                    result.append(node.val)
                    if node.right:
                        queue.append(node.right)
                    
                    if node.left:
                        queue.append(node.left)

                else:
                    node = queue.popleft()
                    
                    if node.right:
                        queue.append(node.right)
                        
                    if node.left:
                        queue.append(node.left)


        return result

