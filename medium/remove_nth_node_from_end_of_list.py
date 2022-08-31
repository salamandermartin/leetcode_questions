# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        dummy = ListNode()
        dummy.next = head
        
        while curr != None:
            length += 1
            curr = curr.next
            
        curr = dummy
        
        length = length - n + 1 
        
        while length > 0:
            prev = curr
            curr = curr.next
            length -= 1
            
        temp = curr
        prev.next = curr.next
        temp.next = None
        
        return dummy.next
        