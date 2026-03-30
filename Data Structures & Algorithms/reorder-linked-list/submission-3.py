# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #[2,4,7,6,8]
        #     ^
        #          ^

        #find halves
        curr = head
        front = head.next

        while front and front.next:
            curr = curr.next
            front = front.next.next
        
        l1 = head
        l2 = curr.next
        curr.next = None
        #reverse
        prev = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        l2 = prev

        #merge
        #[2,4]
        #[8,6,7]
        while l2:
            temp = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp
            l1 = temp
            l2 = temp2
        
        