# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()

        queue.append(root)
        result = []


        while queue:
            rightSide = None

            for _ in range(len(queue)):
                node = queue.popleft()

                if node: 
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightSide:
                result.append(rightSide.val)


        return result