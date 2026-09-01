from typing import Dict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cache_s: Dict[int, int] = dict()
        cache_t: Dict[int, int] = dict()

        for c in s:
            cache_s[c] = cache_s.get(c, 0) + 1

        for c in t:
            cache_t[c] = cache_t.get(c, 0) + 1

        if len(cache_s) != len(cache_t):
            return False
        
        for k, v in cache_s.items():
            if k not in cache_t or cache_t[k] != cache_s[k]:
                return False

        return True
    
    def isAnagram_1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cache_s: Dict[int, int] = dict()

        for c in s:
            cache_s[c] = cache_s.get(c, 0) + 1

        for c in t:
            if c not in cache_s:
                return False
            cache_s[c] = cache_s[c] - 1
            if cache_s[c] < 0:
                return False
            if cache_s[c] == 0:
                del cache_s[c]

        return len(cache_s) == 0
    
s = Solution()

print(s.isAnagram("", ""))
print(s.isAnagram("aba", "bab"))
print(s.isAnagram("abbadca", "aaabbcd"))
print("-----------------------")
print(s.isAnagram_1("", ""))
print(s.isAnagram_1("aba", "bab"))
print(s.isAnagram_1("abbadca", "aaabbcd"))
