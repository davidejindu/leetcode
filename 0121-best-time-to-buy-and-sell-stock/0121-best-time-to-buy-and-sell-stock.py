"""
want to max profit by choosing a single day to buy one stock and another day in the future to sell
so want to buy low and sell high

return max profit you can achieve from this, if its negative return 0

input = 7, 1, 5, 3, 6, 4
output = 5

buy at 1 and sell at 6

have two pointers l and r 
if prices[l] < prices[r]
set l to r
calculate maxx by doing prices[r] - prices[l]


"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = l = 0

        for r in range(1, len(prices)):
            maxx = max(maxx, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l = r

        return maxx