# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Determine list length
        length = 1
        cur = head
        while cur.next:
            length += 1
            cur = cur.next

        # Traverse to middle
        half = length // 2
        cur = head
        i = 0
        while (i != half):
            cur = cur.next
            i += 1

        # Reverse second half
        prev = None
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

        # Compare
        second_half = prev
        first_half = head
        while second_half and first_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True


s = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(2)
node5 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


print(s.isPalindrome(node1))
