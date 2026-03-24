# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """

        make a queue append all values in root
        then sort 
        
        then loop until k

        that would be o(n log kn)

        """


        queue = collections.deque()
        kth_list = []
        queue.append(root)

        while queue:
            
            for _ in range(len(queue)):

                node = queue.popleft()
                if node:
                    kth_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

        
        print(kth_list.sort())
        return kth_list[k - 1]
            

        