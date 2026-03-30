# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # if head.next is None:
        #     return None

        slow = fast = head

        #[1,2,3,4,5,6,7]

        while n > 0 and fast:
            fast = fast.next
            n -= 1

        if fast is None:
            return head.next
            
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next
        return head
