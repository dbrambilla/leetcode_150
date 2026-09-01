from typing import Set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        chars: Set[int] = set()
        l: int = 0
        r: int = 0
        maxl: int = 0

        while r < len(s):
            c: int = s[r]
            if c not in chars:
                chars.add(c)
            else:
                maxl = max(maxl, r - l)
                while s[l] != c:
                    if s[l] in chars:
                        chars.remove(s[l])
                    l += 1
                l += 1
            r += 1
        return maxl
    
s = Solution()

print(s.lengthOfLongestSubstring("zxyzxyz"))