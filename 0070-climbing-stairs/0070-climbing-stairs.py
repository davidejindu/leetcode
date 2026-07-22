"""

want to know how many unique ways you can reach the top

we know that if the top is 1 it takes 1 2 it takes 2 and 3 it takes 3

we can recurse so if we are at 4 we know 3 is 3 unique ways and 4 - 3 is 1 so then we know thats 
already in our memo so its 4 




"""
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2, 3:3}

        def climb(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = climb(x - 2) + climb(x - 1)
                return memo[x]


        return climb(n)
        