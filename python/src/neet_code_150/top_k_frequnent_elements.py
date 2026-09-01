from typing import List, Dict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts: Dict[int, int] = dict()
        top_k: Dict[int, Dict[int, int]] = dict()

        for num in nums:
            curr_count: int = counts.get(num, 0)
            if curr_count > 0:
                del top_k[curr_count][num]
            counts[num] = curr_count + 1
            if (curr_count + 1) not in top_k:
                top_k[curr_count + 1] = dict()    
            top_k[curr_count + 1][num] = 1


        result: List[int] = []
        value: int = len(nums)

        while len(result) < k:
            values: Dict[int, int] = top_k.get(value)
            if values:
                for inner_k in values.keys():
                    result.append(inner_k)
                    if len(result) == k:
                        return result
            value -= 1

        return result
    
    def topKFrequent_optimal(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
    
s = Solution()

print(s.topKFrequent(nums = [1,2,2,3,3,3], k = 2))
print(s.topKFrequent(nums = [7, 7], k = 1))
