# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = deque([root])
        res = ""
        while nodes:
            node = nodes.popleft()
            if node:
                nodes.append(node.left)
                nodes.append(node.right)
                res += str(node.val) + "#"
            else:
                res += "N" + "#"
        return res[:-1]
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split("#")
        for idx, val in enumerate(nodes):
            if val == "N":
                nodes[idx] = None
            else:
                nodes[idx] = TreeNode(int(val))

        if not nodes:
            return None
        if len(nodes) == 1:
            return nodes[0]
        
        root = nodes[0]
        next_node = deque([nodes[0]])
        nodes = deque(nodes[1:])
        while next_node:
            node = next_node.popleft()
            if node:
                left = nodes.popleft()
                right = nodes.popleft()
                node.left = left
                node.right = right
                next_node.append(left)
                next_node.append(right)
        return root