# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

want to return the values of nodes i can see from the right side

so want to keep track of the level the node is on and the node 

i want to append the right node first and then left if it exists

so i want to append the first node from that level to the result array
then pop the other nodes that have that level from the array after first adding its children
to the queue

    
queue = [(1,2)]
result = [1,3]
level = 1
self.level = 2


"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.level = 0
        queue = deque([root])
        result = []


        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == 0:
                    result.append(node.val)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)


        return result

            

           