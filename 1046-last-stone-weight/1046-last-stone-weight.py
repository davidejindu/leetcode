import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        make a max heap

        always pop two and if the first one - second isnt equal to 0
        then add the difference between when the list == 1 return 
        stones[0]
    

        -2, -7, -4 -1 -8 -1
         




        """
      
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            val = (-first) - (-second)
            

            
            if val != 0:
                heapq.heappush(stones,-val)

        return -stones[0] if len(stones) else 0

            





        