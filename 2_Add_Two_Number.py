from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr  = None
        carry = 0
        head  = None

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            
            if l2:
                carry += l2.val
                l2 = l2.next
            if not curr:
                curr = ListNode(carry % 10)
                head = curr
            else:
                curr.next = ListNode(carry % 10)
                curr = curr.next
            carry //= 10
        
        return head
