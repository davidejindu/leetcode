"""
okay so im giving points and want to find the k closes points
ik the first section added to a heap is how it gets ordered

so im wonderingif i can have a heap that has the value of it and then second the points
then i pop k times until i get the coordinates and return that



"""
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for x, y in points:
            val = x**2 + y**2
            heapq.heappush(heap, (val, [x,y]))

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])


        return result

        