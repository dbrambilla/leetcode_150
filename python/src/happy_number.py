import functools

class Solution:
    @functools.cache
    def compute(self, n):
        res = 0
        v = 10
        while n != 0:
            digit = n % 10
            res += digit * digit
            n = n // 10
        return res
    
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.compute(self.compute(n))
        
        while fast != 1:
            # print(f"{slow} and {fast}")
            if slow == fast:
                return False
        
            slow = self.compute(slow)
            fast = self.compute(self.compute(fast))
    
        return True
    
s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))

    