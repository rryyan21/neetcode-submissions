# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head,head #slow = mid 
        
        while fast.next and fast.next.next: 
            slow = slow.next 
            fast = fast.next.next 
            
        #cut off slow.next for 2 lists
        prev, curr = None, slow.next 
        slow.next = None 
        
        #now reverse from mid to end 
        while curr: 
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
            
        left, right = head, prev 
        
        #iterate first, last, second, second-last
        while right: 
            templ = left.next 
            tempr = right.next 
            left.next = right 
            right.next = templ 
            left = templ 
            right = tempr