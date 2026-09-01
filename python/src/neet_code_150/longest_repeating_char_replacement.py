class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [0] * 26
        l: int = 0
        r: int = 0
        m: int = 0
        result: int = 0

        while r < len(s):
            chars[ord(s[r]) - ord('A')] += 1
            size = sum(chars)
            m = max(chars)
            if size - m > k:
                chars[ord(s[l]) - ord('A')] -= 1
                l += 1
                size = sum(chars)
                m = max(chars)
                while size - m > k:
                    chars[ord(s[l]) - ord('A')] -= 1
                    l += 1
                    size = sum(chars)
                    m = max(chars)
            result = max(result, sum(chars))
            r += 1

        return result
    
s = Solution()

print(s.characterReplacement(s="ABAA", k=0))

print(s.characterReplacement("AAABABA", k = 1))
print(s.characterReplacement("AAABABA", k = 2))

