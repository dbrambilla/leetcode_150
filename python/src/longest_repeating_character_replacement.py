import math


class Solution:
    def characterReplacement_2(self, s: str, k: int) -> int:
        # Array to store the count of each uppercase English character (A-Z)
        count = [0] * 26
        
        # Left pointer of the sliding window
        left = 0
        
        # Maximum frequency of any character within the current window
        max_frequency = 0
        
        # Length of the input string
        n = len(s)
        
        # Iterate through the string with the right pointer
        for right in range(n):
            # Increment the count of the current character and update max_frequency
            # ord(char) - ord('A') converts the character to an index (0-25)
            current_char_idx = ord(s[right]) - ord('A')
            count[current_char_idx] += 1
            max_frequency = max(max_frequency, count[current_char_idx])
            
            # Check if current window is invalid (requires more than k replaces)
            # A window is invalid if window_size - max_frequency > k
            if (right - left + 1) - max_frequency > k:
                print(f"{count} - [{left}, {right}]")
                # If invalid, shrink the window from the left
                # Decrement the count of the character at the left pointer
                left_char_idx = ord(s[left]) - ord('A')
                count[left_char_idx] -= 1
                # Move the left pointer to the right
                left += 1
                
            # At this point, the window is always valid, and maximizing size.
            
        # The maximum length is the length of the final, longest valid window
        return n - left

    def characterReplacement(self, s: str, k: int) -> int:
        l: int = 0
        r: int = 0
        res: int = 0
        cache = {}

        while r < len(s):
            c = s[r]
            if c not in cache and len(cache) == 2:
                while s[l] in cache:
                    cache[s[l]] -= 1
                    if cache[s[l]] == 0:
                        del cache[s[l]]
                        l += 1
                        break
                    l += 1
            elif c in cache and len(cache) == 2:
                keys = list(cache.keys())
                # print(f"KEYS: {keys} - ({l}, {r})")
                if min(cache[keys[0]], cache[keys[1]]) == k:
                    while s[l] != c:
                        cache[s[l]] -= 1
                        if cache[s[l]] == 0:
                            del cache[s[l]]
                        l += 1
            cache[c] = cache.get(c, 0) + 1
            # print(f"{cache} - ({l}, {r})")
            res = max(res, (r - l + 1))
            r += 1

        return res

s = Solution()
# print(s.characterReplacement("aacd", 4))
# print(s.characterReplacement("aaad", 4))
# print(s.characterReplacement("aaaddaa", 1))
# print(s.characterReplacement_2("AAADA", 0))
print(s.characterReplacement_2("AAAABBBAA", 2))