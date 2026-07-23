"""

input = [1,2,5], amount = 11

amount = 3

the goal is bottom up dp

you want base case we know at coin 1 the fewest number of coins is 1

so have an array dp that has index 0 all the way to amount + 1 so we get the amount number

then have them all set to 1

0 1 2 3 4 5 6 7 8 9 10 11
0 1 2 3 4 5 6 7 8 9 10 11

have a minn variable to store the min of coins required for each coin
skip 1 so we start loop at 2

you loop through the coins array and subtract by i so 2 - 1 = 1 

ik how to solve this problem 



"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            minn = float('inf')

            for coin in coins:
                diff = i - coin

                #if coin is greater than index you cant the diff
                if diff < 0:
                    break

                minn = min(minn, 1 + dp[diff])

            dp[i] = minn

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]