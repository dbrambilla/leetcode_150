class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cache = [0] * 26
        chars = set()
        
        for c in s1:
            cache[ord(c) - ord('a')] += 1
            chars.add(c)

        l: int = 0
        r: int = 0
        while r < len(s2):
            c = s2[r]
            
            if c in chars:
                if cache[ord(c) - ord('a')] == 0:
                    while s2[l] != c:
                        if s2[l] in chars:
                            cache[ord(s2[l]) - ord('a')] += 1
                        l += 1
                else :
                    # Decrement character c in cache
                    cache[ord(c) - ord('a')] -= 1
                    # If cache sum is 0 we removed all the characters in order and we found a permutation
                    if sum(cache) == 0:
                        return True
            else:
                # We need to reset the search and move l to r
                while l < r:
                    if s2[l] in chars:
                        cache[ord(s2[l]) - ord('a')] += 1
                    l += 1
            r += 1

        return False

s = Solution()

print(s.checkInclusion(s1="adc", s2="dcda"))
print(s.checkInclusion(s1 = "abc", s2 = "lecabee"))
print(s.checkInclusion(s1 = "abc", s2 = "lecaabee"))
