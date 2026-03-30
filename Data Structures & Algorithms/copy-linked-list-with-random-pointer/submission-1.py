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
        nodes = {}
        res = dummy = head

        while head:
            new_node = Node(head.val, head.next, head.random)
            nodes[head] = new_node
            head = head.next

        while dummy:
            if not dummy.next:
                nodes[dummy].next = None
            else:
                nodes[dummy].next = nodes[dummy.next]
            if not dummy.random:
                nodes[dummy].random = None
            else:
                nodes[dummy].random = nodes[dummy.random]
            dummy = dummy.next

        if res:
            return nodes[res]
        return res