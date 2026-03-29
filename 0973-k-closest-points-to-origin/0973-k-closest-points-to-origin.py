class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        """
        okay so loop through each points
        get the calculation and the points
        heappush(points, calculation, points[i])
        then for i in range(k) keep popping and append points[i] to result list
        """

        result = []
        heapify(result)


        res = []

        
        for i in range(len(points)):
            the_point = points[i]
            val = ((the_point[0] * the_point[0]) + the_point[1] * the_point[1])
            heapq.heappush(result,(val,the_point))

        
        for i in range(k):
            val, points = heapq.heappop(result)
            res.append(points)

        return res


