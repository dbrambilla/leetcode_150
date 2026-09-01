from typing import List
class Solution:
    def findDuplicate_binary_search(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 1, n - 1
        while low < high:
            mid = low + (high - low) // 2
            lessOrEqual = sum(1 for num in nums if num <= mid)

            if lessOrEqual <= mid:
                low = mid + 1
            else:
                high = mid

        return low
    def findDuplicate_slow_fast_pointers(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow