from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        START: int = 0
        END: int = 1
        result: List[List[int]] = []
        intervals.sort(key=lambda x: x[0])
        curr: List[int] = intervals[0][:]
        for i in range(1, len(intervals)):
            interval: List[int] = intervals[i]
            if curr[END] >= interval[START]:
                # Merge and update curr
                curr[END] = max(curr[END], interval[END])
            else:
                # Save the interval
                result.append(curr)
                curr = interval
        result.append(curr)

        return result


s = Solution()

print(s.merge(intervals = [[1,3],[1,5],[6,7]]))