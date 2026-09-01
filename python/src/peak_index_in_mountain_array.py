from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l: int = 0
        r: int = len(arr) - 1

        while l < r:
            m: int = l + ( r - l ) // 2
            if arr[m] < arr[m+1]:
                l = m + 1
            else:
                r = m
        return l
            


s = Solution()

# print(s.peakIndexInMountainArray([0,10,5,2]))
# print(s.peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))
print(s.peakIndexInMountainArray([12,13,19,41,55,69,70,71,96,72]))