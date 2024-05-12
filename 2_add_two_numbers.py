#!/usr/bin/python3
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(val=0)
        tail = dummy_head
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            digit_1 = l1.val if l1 != None else 0
            digit_2 = l2.val if l2 != None else 0
            sum = digit_1 + digit_2 + carry
            carry = sum // 10
            actual_digit = sum % 10
            new_node = ListNode(val=actual_digit)
            tail.next = new_node
            tail = tail.next
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        
        result = dummy_head.next
        dummy_head.next = None
        return result

s = Solution()
l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
result = s.addTwoNumbers(l1, l2)
while result != None:
    print(result.val)
    result = result.next