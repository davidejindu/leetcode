"""

go through the stones list and turn them all into negative and add them to heap
then pop the top two and then whatever is greater is y the other is x

if they are both equal dont add anything back but if not equal then add y - x to heap



"""
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)


        while heap and len(heap) > 1:
            val1, val2 = -heapq.heappop(heap), -heapq.heappop(heap)

            if val1 > val2:
                y = val1
                x = val2
            else:
                y = val2
                x = val1

            if y != x:
                new_weight = y - x
                heapq.heappush(heap, -new_weight)

        if not heap:
            return 0 
        else:
            return -heap[0]

        