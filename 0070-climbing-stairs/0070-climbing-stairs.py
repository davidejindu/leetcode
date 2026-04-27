class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        def climb(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = climb(x - 1) + climb(x - 2)
                return memo[x]

        return climb(n)