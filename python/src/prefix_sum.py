class Solution:
    def prefix_sum(self, nums: list[int]):
        result: list[int] = [0] * len(nums)
        result[0] = nums[0]

        for i in range(1, len(nums)):
            result[i] = nums[i] + result[i-1]

        return result
    
    def query(self, prefix_sum: list[int], i: int, j: int):
        if i == 0:
            return prefix_sum[j]
        return prefix_sum[j] - prefix_sum[i-1] 
    
s = Solution()
o = [1,3,4,5,1,2,1]
p = s.prefix_sum(o)
print(o)
print(p)
print(s.query(p, 0, 4))
print(s.query(p, 2, 4))