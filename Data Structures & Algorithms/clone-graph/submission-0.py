"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(node):
            if not node:
                return None
            seen[node] = new_node = Node(node.val)
            for n in node.neighbors:
                if n not in seen:
                    new_node.neighbors.append(dfs(n))
                else:
                    new_node.neighbors.append(seen[n])
            return new_node
        
        return dfs(node)