from typing import List, Set
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        def bt(nums: List[List[int]], result: List[List[int]], indexes: Set[int], partial: List[int]):
            if len(partial) == len(nums):
                copy = partial.copy()
                result.append(copy)
                return 
            
            for i in range(len(nums)):
                if i not in indexes:
                    indexes.add(i)
                    partial.append(nums[i])
                    bt(nums, result, indexes, partial)
                    partial.pop()
                    indexes.remove(i)
                
        bt(nums, result, set(), [])

        return result
    
s = Solution()

print(s.permute([1,2,3]))