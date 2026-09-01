from typing import Optional
from ds import ListNode
from utils import print_linked_list, create_linked_list

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head: ListNode = ListNode(0)
        current: ListNode = head
        carry: int = 0

        while l1 and l2:
            v1, v2 = int(l1.val), int(l2.val)
            nv: int = v1 + v2 + carry
            if nv >= 10:
                nv = nv % 10
                carry = 1
            else:
                carry = 0
            current.next = ListNode(nv)
            current = current.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            v1 = int(l1.val)
            nv: int = v1 + carry
            if nv >= 10:
                nv = nv % 10
                carry = 1
            else:
                carry = 0
            current.next = ListNode(nv)
            current = current.next
            l1 = l1.next
        
        while l2:
            v2 = int(l2.val)
            nv: int = v2 + carry
            if nv >= 10:
                nv = nv % 10
                carry = 1
            else:
                carry = 0
            current.next = ListNode(nv)
            current = current.next
            l2 = l2.next

        if carry == 1:
            current.next = ListNode(carry)
            
        return head.next
    
s = Solution()

l1 = create_linked_list([1,2,3])
l2 = create_linked_list([4,5,6])
print_linked_list(s.addTwoNumbers(l1, l2))


l1 = create_linked_list([9,9])
l2 = create_linked_list([9,5,6])
print_linked_list(s.addTwoNumbers(l1, l2))