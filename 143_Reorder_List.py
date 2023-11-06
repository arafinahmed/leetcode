from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s_pointer = head
        f_pointer = head.next

        while f_pointer and f_pointer.next:
            s_pointer = s_pointer.next
            f_pointer = f_pointer.next.next

        second_head = s_pointer.next
        prev = s_pointer.next = None

        
        while second_head:
            next = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = next

        second_head = prev
        first_head = head

        while second_head:
            temp1, temp2 = first_head.next, second_head.next
            first_head.next = second_head
            second_head.next = temp1
            first_head, second_head = temp1, temp2
