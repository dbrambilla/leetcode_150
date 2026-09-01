from typing import List

"""
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Convert list to a set for O(1) lookups
        word_set = set(wordDict)
        
        # dp[i] will be True if s[0:i] can be segmented into words
        dp = [False] * (len(s) + 1)
        
        # Base case: an empty string is a valid segmentation
        dp[0] = True
        
        # Iterate through all ending positions of substrings
        for i in range(1, len(s) + 1):
            # Iterate through all possible split points
            for j in range(i):
                # If the prefix s[0:j] is valid AND the suffix s[j:i] is in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Move to the next index 'i' once true
                    
        return dp[len(s)]

            