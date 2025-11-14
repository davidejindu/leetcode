class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = []

        if len(cost) < 1:
            return 0

        if len(cost) == 1:
            return cost[0]

        if len(cost) == 2:
            return min(cost[0], cost[1])

        for i in range(len(cost)):
            if i == 0 or i == 1:
                memo.append(cost[i])
            else:
                memo.append(cost[i] + min(memo[i -1], memo[i - 2]))
           

        print(memo)

        return min(memo[len(memo) - 2], memo[len(memo) - 1])
               
            
