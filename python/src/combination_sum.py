from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []

        def bt(index:int, current_list:List[int], current_sum:int):
            if current_sum == target:
                result.append(current_list.copy())
                return
            
            if current_sum > target:
                return
            
            for i in range(index, len(candidates)):
                current_list.append(candidates[i])
                current_sum += candidates[i]
                bt(i, current_list, current_sum)
                current_list.pop()
                current_sum -= candidates[i]

        bt(0, [], 0)
        return result
    
s = Solution()

print(s.combinationSum([2,3,6,7], target = 7))