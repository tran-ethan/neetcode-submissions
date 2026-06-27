# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None # Node before the element to be removed
        curr = head
        reLink = None

        while curr:
            if curr.val == val and not reLink:
                reLink = prev
            elif reLink and curr.val != val:
                reLink.next = curr
                reLink = None

            prev = curr
            curr = curr.next
        
        if reLink:
            reLink.next = None
        
        if head and head.val == val:
            head = head.next

        return head