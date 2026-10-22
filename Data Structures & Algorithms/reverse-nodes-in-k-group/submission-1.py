# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy
        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                break
            nextGroup = kth.next
            prev, curr = nextGroup, prevGroup.next
            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp

        return dummy.next
            
    def getKth(self, head, k):
        while head and k > 0:
            head = head.next
            k -= 1
        return head