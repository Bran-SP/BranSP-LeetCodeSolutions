class Solution:#Given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins needed to reach amount or -1 if it is impossible.
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) #make a big dynamic 2d array
        dp[0] = 0

        for a in range(1, amount + 1):#by finding fewest number of coins needed to reach each number less than amount and saving it, you can build up to the answer
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1