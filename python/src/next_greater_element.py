from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        i: int = len(nums2) - 1
        cache = {}

        while i >= 0:
            v = nums2[i]
            if stack and stack[-1] > v:
                cache[v] = stack[-1]
            else:
                while stack and stack[-1] < v:
                    stack.pop()
                cache[v] = stack[-1] if stack else -1
            stack.append(v)
            i -= 1

        return [cache[c] for c in nums1]
    
s = Solution()
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))