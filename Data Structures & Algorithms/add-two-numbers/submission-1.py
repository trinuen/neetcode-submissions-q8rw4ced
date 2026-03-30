# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = head = ListNode()
        #sum of l1[i] + l2[j] + carry <= 24 will never
        carry = 0
        while l1 or l2:
            if l1 and l2:
                total = l1.val + l2.val + carry
            elif l1:
                total = l1.val + carry
            else:
                total = l2.val + carry
            #find new carry
            if total >= 20:
                carry = 2
                new_val = total - 20
                new_node = ListNode(new_val)
                head.next = new_node
            elif total >= 10:
                carry = 1
                new_val = total - 10
                new_node = ListNode(new_val)
                head.next = new_node
            else:
                carry = 0
                new_node = ListNode(total)
                head.next = new_node

            if l1 and l2:
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l1 = l1.next
            else:
                l2 = l2.next
            head = head.next

        if carry != 0:
            new_node = ListNode(carry)
            head.next = new_node

        return dummy.next

        

            
                