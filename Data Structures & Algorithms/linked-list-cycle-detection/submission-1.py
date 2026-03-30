# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr, front = head, head

        while front and front.next:
            curr = curr.next
            front = front.next.next
            if front == curr:
                return True
        return False