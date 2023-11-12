from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head
        ans_head = None
        ans_tail = None
        while True:
            for i in range(k):
                if not fast:
                    return ans_head
                fast = fast.next
            
            head = self.reverseList(slow, fast)

            if not ans_head:
                ans_head = head
            if ans_tail:
                ans_tail.next = head
            ans_tail = slow
            slow = fast
        return ans_head

    def reverseList(self, slow, fast):
        prev = fast
        while slow != fast:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        return prev