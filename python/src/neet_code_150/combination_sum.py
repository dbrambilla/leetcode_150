from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []
        nums.sort()

        def rec(nums: List[int], target: int, index: int, partial: List[List[int]], result: List[List[int]]):
            if index == len(nums):
                return
            
            partial_sum: int = sum(partial)
            for i, num in enumerate(nums):
                if i < index:
                    continue
                
                if partial_sum + num == target:
                    solution: List[int] = partial.copy()
                    solution.append(num)
                    result.append(solution)
                
                if partial_sum + num < target:
                    partial.append(num)
                    rec(nums, target, i, partial, result)
                    partial.pop()
                else:
                    break

        rec(nums, target, 0, [], result)
        return result
    
s = Solution()

print(s.combinationSum(nums = [2,5,6,9], target = 9))