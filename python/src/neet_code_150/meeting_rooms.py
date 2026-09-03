from typing import List
from ds import Interval

def compare(x: Interval, y: Interval) -> int:
    return x.start - y.start

class Solution:    
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(
            key=lambda interval: interval.start
        )
        i: int = 1
        last_end: int = intervals[0].end
        while i < len(intervals):
            if last_end > intervals[i].start:
                return False
            last_end = max(last_end, intervals[i].end)
            i += 1
        return True

s = Solution()

print(s.canAttendMeetings([Interval(10,30),Interval(5,10),Interval(15,20)]))
print(s.canAttendMeetings([Interval(5,8),Interval(9,15)]))