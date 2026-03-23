# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        make a queue FIFO
        append root to it first
        """


        queue = collections.deque()

        queue.append(root)
        
        level_order_list = []
        while queue:
            queue_list = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if queue_list:
                level_order_list.append(queue_list)

        return level_order_list



        