from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge cases
        if len(s) <= 1:
            return len(s)
        
        l: int = 0
        cache: Dict[int, int] = dict()
        longest: int = 0

        cache[s[l]] = 0
        for r in range(1, len(s)):
            if s[r] in cache and cache[s[r]] >= l:
                l = cache[s[r]]
            cache[s[r]] = r
            longest = max(longest, (r - l + 1))

        return longest