from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = [[]]

        for num in nums:
            partial_results: List[List[int]] = []
            for res in result:
                copy = res.copy()
                copy.append(num)
                partial_results.append(copy)
            result.extend(partial_results)

        return result
    
    def subsets_rec(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def bb(nums, index, result):
            if index < len(nums):
                num = nums[index]
                partial_results: List[List[int]] = []
                for res in result:
                    copy = res.copy()
                    copy.append(num)
                    partial_results.append(copy)
                result.extend(partial_results)
                bb(nums, index+1, result)

        bb(nums, 0, result)
        return result
    
s = Solution()

print(s.subsets([1,2,3]))
print(s.subsets_rec([1,2,3]))
