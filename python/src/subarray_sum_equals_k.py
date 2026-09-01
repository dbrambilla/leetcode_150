from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        
        res: int = 0
        l: int = 0
        r: int = 0
        curr_sum: int = 0

        while r < len(nums):
            curr_sum += nums[r]
            while curr_sum >= k:
                if curr_sum == k:
                    res += 1
                curr_sum -= nums[l]
                l += 1
            r += 1

        return res
    
    def subarraySum_prefix_sum(self, nums: List[int], k: int) -> int:
        cache: Map[int, int] = {0: 1}
        partial_sum: int = 0
        count: int = 0

        for num in nums:
            partial_sum += num
            key: int = partial_sum - k
            if key in cache:
                count += cache[key]
            cache[partial_sum] = cache.get(partial_sum) + 1 if partial_sum in cache else 1

        return count
    
s = Solution()
print(s.subarraySum([1,1,1], 2))
print(s.subarraySum([1,2,3], 3))