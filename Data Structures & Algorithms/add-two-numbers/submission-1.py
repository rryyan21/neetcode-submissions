# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0 

        while l1 or l2:
            #sum = digit1 + digit2 + carry 
            dig1 = l1.val if l1 else 0 
            dig2 = l2.val if l2 else 0 
            total = dig1 + dig2 + carry

            digit = total % 10
            carry = total // 10

            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next if l1 else 0 
            l2 = l2.next if l2 else 0 

        if carry:
            curr.next = ListNode(carry)
        return dummy.next

            