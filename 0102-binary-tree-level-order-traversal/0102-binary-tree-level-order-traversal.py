from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        bfs does this exactly

        make a queue
        store the root as first value in queue

        loop through len of queue 
        pop first value in queue append it to list
        then if first value has children add it to queue
        after loop ends add list of appends to the result list
        when queue is empty break out of main while loop and return result

        """


        if root is None:
            return []


        queue = deque([root])
        result = []

        while len(queue) > 0:

            level_list = []
            for _ in range(len(queue)):
                node_in_queue = queue.popleft()
                level_list.append(node_in_queue.val)

                if node_in_queue.left:
                    queue.append(node_in_queue.left)

                if node_in_queue.right:
                    queue.append(node_in_queue.right)

            result.append(level_list)

        return result


