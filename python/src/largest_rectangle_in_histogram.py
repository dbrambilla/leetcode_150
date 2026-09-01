from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        i: int = 0
        res: int = 0

        while i < len(heights):
            h = heights[i]
            if stack and h <= stack[-1][0]:
                while stack and h <= stack[-1][0]:
                    idx = stack.pop()[1]
                stack.append([h, idx])
                for (v,idx) in stack:
                    res = max(res, min(v, h) * (i - idx + 1))
            elif stack and h > stack[-1][0]:
                stack.append([h, i])
                for (v,idx) in stack:
                    res = max(res, min(v, h) * (i - idx + 1))
            else:
                stack.append([h, i])
                res = max(res, h * (i - 0 + 1))
            print(f"{i}: {stack} with res {res}")
            i += 1

        return res
    
    def largestRectangleArea_optimized(self, heights):
        stack = []  # stores indices
        max_area = 0
        n = len(heights)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))

        for idx, height in stack:
            max_area = max(max_area, height * (n - idx))

        return max_area


s = Solution()
# print(s.largestRectangleArea([2,1,5,6,2,3]))
# print(s.largestRectangleArea([2,4]))
# print(s.largestRectangleArea([0,9]))
print(s.largestRectangleArea([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))