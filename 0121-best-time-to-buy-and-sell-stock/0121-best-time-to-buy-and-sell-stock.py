"""

7,1,5,3,6,4
l
r

if its less than 0 make it 0

so your gonna increment through prices with r pointer
if r value is less than l than make l that thats only when you change it

each time calculate profit if profit is greater than max_profit




"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_money = 0
        l = 0

        for r in range(1,len(prices)):
            profit = prices[r] - prices[l]
            max_money = max(max_money, profit)

            if prices[l] > prices[r]:
                l = r

        return max_money