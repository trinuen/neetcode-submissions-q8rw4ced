# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy
        while True:
            kth = self.getKth(prev_group, k)
            if not kth:
                break
            next_group = kth.next

            prev, curr = next_group, prev_group.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp

        return dummy.next
    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node