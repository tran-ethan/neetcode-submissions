# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0

        head = ListNode()
        prev = None
        curr = head

        while carry != 0 or curr1 or curr2:
            total = carry
            if curr1:
                total += curr1.val
                curr1 = curr1.next
            if curr2:
                total += curr2.val
                curr2 = curr2.next
            sum = total % 10    # sum digit
            carry = total // 10 # carry digit
            # print(sum, carry)
            curr.val = sum

            curr.next = ListNode()
            prev = curr
            curr = curr.next

        prev.next = None
        return head
        