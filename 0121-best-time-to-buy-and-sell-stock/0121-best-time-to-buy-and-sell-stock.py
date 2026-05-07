class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

         7,1,5,3,6,4
         l
            r

        minimum = 7
        max = 5



        want to keep track of minimum
        only increase if r is less than minimum
        keep getting max



        """

        max_profit = 0
        l = 0

        for r in range(1,len(prices)):
            if prices[r] - prices[l] > 0:
                max_profit = max(max_profit,prices[r] - prices[l] )

            if prices[r] < prices[l]:
                l = r

        return max_profit




        return max_profit
            



        