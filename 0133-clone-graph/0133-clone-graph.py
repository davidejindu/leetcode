"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
            
        nodeMap = {}

        def clone(node):
            if node in nodeMap:
                return nodeMap[node]

            new_node = Node(node.val)
            nodeMap[node] = new_node

            for neighbor in node.neighbors:
                new_node.neighbors.append(clone(neighbor))

            return new_node

        return clone(node)