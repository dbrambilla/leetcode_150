class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # Initialize DP table with False values
        # Size is (m + 1) x (n + 1) to accommodate empty string/pattern base cases
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base Case: An empty string matches an empty pattern
        dp[0][0] = True
        
        # Base Case: Deal with patterns that can match an empty string (e.g., "a*", "a*b*", ".*")
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Fill the DP table sequentially
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If current pattern character is a star '*'
                if p[j - 1] == '*':
                    # Case 1: Count star as 0 occurrences of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case 2: Count star as 1 or more occurrences (if preceding character matches)
                    preceding_char = p[j - 2]
                    if preceding_char == s[i - 1] or preceding_char == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
                # If current pattern character is a letter or '.'
                else:
                    if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
            print(dp)
                        
        # The bottom-right cell holds the answer for the full string and pattern
        return dp[m][n]

s = Solution()

print(s.isMatch(s = "aaaaaaaa", p = "a*"))