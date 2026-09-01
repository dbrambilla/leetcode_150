from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()        
        curr: List[int] = [0] * (amount+1)

        coin = coins[0]
        for i in range(coin, amount + 1, coin):
            curr[i] = curr[i - coin] + 1

        for coin in coins[1:]:
            for i in range(coin, amount + 1):
                if coin == i:
                    curr[i] = 1
                else:    
                    if curr[i-coin] != 0:
                        if curr[i] == 0:
                            curr[i] = curr[i-coin] + 1
                        else:
                            curr[i] = min(curr[i], curr[i-coin] + 1)
        print(curr)
        return curr[amount] if curr[amount] != 0 else -1
    
    def coinChange_2(self, coins: list[int], amount: int) -> int:
        # dp[i] will be storing the minimum number of coins required for amount i
        # amount + 1 is a placeholder for infinity
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1

s = Solution()

# print(s.coinChange(coins = [1,2,5], amount = 11))
# print(s.coinChange(coins = [2], amount = 3))
# print(s.coinChange(coins = [1,2], amount = 2))
# print(s.coinChange(coins = [2,5,10,1], amount = 27))
print(s.coinChange(coins = [186,419,83,408], amount = 6249))