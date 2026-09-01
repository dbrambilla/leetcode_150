from ds import ListNode
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy: ListNode = ListNode(-1)
        dummy.next = head
        slow: ListNode = dummy
        fast: ListNode = dummy

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next if slow.next else None

        return dummy.next
        