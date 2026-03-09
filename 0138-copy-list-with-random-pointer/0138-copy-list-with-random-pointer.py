"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        node = head
        copy_node = None

        while node:
            copy_node = Node(node.val)
            oldToCopy[node] = copy_node
            node = node.next

        node = head
        while node:
            copy_node = oldToCopy[node]
            copy_node.next = oldToCopy[node.next]
            copy_node.random = oldToCopy[node.random]
            node = node.next

        return oldToCopy[head]
