class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1. Find the middle point (Slow and Fast Pointers)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        # 'slow' is the end of the first half. 'slow.next' starts the second half.
        curr = slow.next
        slow.next = None  # Split the two lists completely
        
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 3. Merge both halves (Interleave)
        first, second = head, prev
        while second:
            # Save next pointers
            tmp1, tmp2 = first.next, second.next
            
            # Connect nodes
            first.next = second
            second.next = tmp1
            
            # Move pointers forward
            first = tmp1
            second = tmp2