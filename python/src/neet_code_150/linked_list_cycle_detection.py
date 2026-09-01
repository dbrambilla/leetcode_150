from typing import Optional
from ds import ListNode
from utils import print_linked_list, create_linked_list

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow: ListNode = head
        fast: ListNode = head.next.next

        while fast and fast.next:
            if slow.val == fast.val:
                return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        return False
    

