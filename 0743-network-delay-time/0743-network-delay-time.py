class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        storage = defaultdict(list)

        for u, v, w in times:
            storage[u].append((v,w))

        visited = set()
        minHeap = [(0,k)]
        result = 0

        while minHeap:
            weight, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            result = max(result, weight)

            for nei_node, weight2 in storage[node]:
                if nei_node not in visited:
                    heapq.heappush(minHeap, (weight + weight2, nei_node))

        return result if len(visited) == n else -1



