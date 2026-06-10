# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        head = ListNode()
        prev = None
        curr = head

        while carry != 0 or l1 or l2:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            sum = total % 10    # sum digit
            carry = total // 10 # carry digit
            curr.val = sum

            curr.next = ListNode()
            prev = curr
            curr = curr.next

        prev.next = None
        return head
        