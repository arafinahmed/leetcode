from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        head = None

        while list1 and list2:
            if list1.val < list2.val:
                if not head:
                    head = list1
                else:
                    prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                if not head:
                    head = list2
                else:
                    prev.next = list2
                prev = list2
                list2 = list2.next
        
        while list1:
            if not head:
                head = list1
            else:
                prev.next = list1
            prev = list1
            list1 = list1.next
        
        while list2:
            if not head:
                head = list2
            else:
                prev.next = list2
            prev = list2
            list2 = list2.next
        
        return head
    
x = Solution()
x.mergeTwoLists(ListNode(1, ListNode(2, ListNode(3))), ListNode(1, ListNode(2, ListNode(3))))