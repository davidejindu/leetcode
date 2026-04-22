class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        graph = defaultdict(list)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((distance,j))
                graph[j].append((distance,i))


        visited = set()
        minHeap = [(0,0)]
        result = 0

        while len(visited) < len(points):
            cost, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            result += cost
            visited.add(point)

            for distance, neighbor in graph[point]:
                if neighbor not in visited:
                    heapq.heappush(minHeap,(distance, neighbor))

        return result

