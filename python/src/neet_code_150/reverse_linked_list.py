from ds import ListNode
from typing import Optional
from utils import print_linked_list, create_linked_list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev: ListNode = None
        curr: ListNode = head
        next: ListNode = head.next

        while curr:
            prev = curr
            curr.next = prev
            curr = next
            if curr:
                next = curr.next
        
        return prev
    
s = Solution()

print_linked_list(s.reverseList(create_linked_list([0, 1, 2, 3])))