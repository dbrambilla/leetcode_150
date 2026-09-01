import math

class Solution:
    def minWindow_2(self, s: str, t: str) -> str:
        # Initialize frequency map for characters
        char_map = [0] * 128
        for c in t:
            char_map[ord(c)] += 1
            
        # Initialize window variables
        counter = len(t)
        begin = 0
        end = 0
        d = float('inf')
        head = 0
        
        # Slide the window over string s
        while end < len(s):
            # Expand the window
            if char_map[ord(s[end])] > 0:
                counter -= 1
            char_map[ord(s[end])] -= 1
            end += 1
            
            # Contract the window when valid
            while counter == 0:
                if end - begin < d:
                    head = begin
                    d = end - begin
                    
                char_map[ord(s[begin])] += 1
                if char_map[ord(s[begin])] > 0:
                    counter += 1
                begin += 1
                
        return "" if d == float('inf') else s[head:head + d]
   
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        cache = {i: 0 for i in range(0, 128)}
        for c in t:
            cache[ord(c)] += 1

        counter: int = len(t)
        l: int = 0
        r: int = 0
        length: int = math.inf
        head: int = 0

        while r < len(s):
            # register the character
            if ( cache[ord(s[r])] > 0 ):
                # if the cache for the character is greater than 0 it means it is one of the t character
                counter -= 1
            cache[ord(s[r])] -= 1
            r += 1
            
            while counter == 0:
                if ( r - l < length ):
                    length = r - head
                    head = l
                if cache[ord(s[l])] == 0:
                    counter += 1
                cache[ord(s[l])] += 1
                l += 1

        return s[head:(head + length)] if length != math.inf else ""
    

        
s = Solution()
print(s.minWindow("adobecodebanc", "abc"))
print(s.minWindow_2("adobecodebanc", "abc"))