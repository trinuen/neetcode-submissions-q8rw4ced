# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None or head.next is None:
            return False
        
        curr = head
        front = head.next

        while front and curr:
            if front.val == curr.val:
                return True
            curr = curr.next
            if front.next:
                front = front.next.next
            else:
                print("line1")
                return False
        print("line 2")
        return False