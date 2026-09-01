from typing import List, Set

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        def bt(current: List[int], visited: Set[int]):
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in nums:
                if i in visited:
                    continue
                visited.add(i)
                current.append(i)
                bt(current, visited)
                current.pop()
                visited.remove(i)

        bt([], set())
        return result
        
s = Solution()
print(s.permute([1,2,3]))