# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        curr = head

        #use two pointers with distance of n to get to removeable node
        #how to get two pointers in distance of n, use for loop with range n

        #move end by n to keep dist, if end is None then head is removing Node
        for _ in range(n):
            end = end.next

        if end is None:
            head = head.next

        #move curr to the right node to remove
        while end:
            if end.next == None:
                break
            end = end.next
            curr = curr.next

        #remove node
        if curr.next:
            curr.next = curr.next.next

        return head

        

        


        