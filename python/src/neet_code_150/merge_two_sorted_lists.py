from ds import ListNode
from typing import Optional
from utils import create_linked_list, print_linked_list

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy: ListNode = ListNode(-1)
        dummy_head: ListNode = dummy

        while list1 and list2:
            if list1.val <= list2.val:        
                dummy.next = ListNode(list1.val)
                list1 = list1.next
            else:
                dummy.next = ListNode(list2.val)
                list2 = list2.next
            dummy = dummy.next

        while list1:
            dummy.next = ListNode(list1.val)
            list1 = list1.next
            dummy = dummy.next
        
        while list2:
            dummy.next = ListNode(list2.val)
            list2 = list2.next
            dummy = dummy.next
        
        return dummy_head.next
    
s = Solution()

print_linked_list(s.mergeTwoLists(create_linked_list([1,2,5,6]), create_linked_list([3,4,7,8])))