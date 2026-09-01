from ds import ListNode
from typing import List, Optional
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head: ListNode = ListNode(-1)
        dummy: ListNode = head
        heap = []

        for i in range(len(lists)):
            if lists[i]: 
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            value, i, node = heapq.heappop(heap)
            dummy.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            dummy = dummy.next
            node.next = None

        return head.next
