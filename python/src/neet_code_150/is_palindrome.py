class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        if len(s) == 2:
            return s[0].lower() == s[1].lower()

        l: int = 0
        r: int = len(s) - 1

        while l < r:
            lc = s[l].lower()
            while l < r and not lc.isalnum():
                l += 1
                lc = s[l].lower()

            rc = s[r].lower()
            while l < r and not rc.isalnum():
                r -= 1
                rc = s[r].lower()

            if lc != rc:
                return False
            
            l += 1
            r -= 1
        
        return True

s = Solution()

print(s.isPalindrome("a/"))
print(s.isPalindrome("Was it a car or a cat I saw?"))
print(s.isPalindrome("tab a cat"))
print(s.isPalindrome("aga"))


