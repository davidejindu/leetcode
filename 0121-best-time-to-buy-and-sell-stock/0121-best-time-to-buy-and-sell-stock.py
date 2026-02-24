class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
    start l , 0 and r at 1
    if prices[l] < prices[r]:
        maxProfit(maxProfix, prices[r] - prices[l])

    maybe store the min_value if value is minimum then make l = to index of it
    then keep looping r
    [7,1,5,3,6,4]
       l     r
        """

        maxProfit = 0
        l, r = 0,1 

        for r in range(len(prices)):

            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l]) 
            else:
                l = r
                

        return maxProfit


        