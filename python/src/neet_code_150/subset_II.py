from typing import List, Set

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result: Set[List[int]] = [[]]
        nums.sort()
        
        def bb(nums, index, partial, result):
            if index < len(nums):
                subsets = []
                if index > 0 and nums[index - 1] == nums[index]:
                    subsets = partial
                else:
                    subsets = result

                num = nums[index]
                partial_results: List[List[int]] = []
                for res in subsets:
                    copy = res.copy()
                    copy.append(num)
                    partial_results.append(copy)
                result.extend(partial_results)
                bb(nums, index + 1, partial_results, result)

                    
        bb(nums, 0, result, result)
        return result
    
    def subsetsWithDup_2(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

s = Solution()

print(s.subsetsWithDup_2([1,2,1,1])) 
print(s.subsetsWithDup([1,2,1,1])) 
"""
[[]]
num = 1, index = 0
[] + 1
[[], [1]]
num = 1, index = 1, [[], [1]]
[] + 1, [1] + 1 ==> [1], [1,1] ==> [1] duplicate
num = 1, index = 1, [[1]]
[[1], [1,1]]
if next == prev 
[[], [1]] and then 2,2
[[],[1],[2],[1,2]]
[[2], [1,2]] => [[2,2], [1,2,2]] another 2
[[2,2], [1,2,2]] => [[2,2,2], [1,2,2,2]]



"""