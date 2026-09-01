from typing import List, Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache: Dict[str, List[str]] = dict()

        for s in strs:
            check: str = ''.join(sorted(s))    
            if check not in cache:
                cache[check] = []
            cache[check].append(s)

        return [v for v in cache.values()]

s = Solution()

print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))