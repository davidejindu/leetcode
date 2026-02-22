import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v, time in times:
            graph[u].append((v,time))

        min_heap = [(0,k)]
        min_times = {}

        """
{2:[(1,1), (3,1)], 3: [(4,1)]}

        """

        while len(min_heap) > 0:
            time_k_to_node, node = heapq.heappop(min_heap)
            if node in min_times:
                continue

            min_times[node] = time_k_to_node

            for neighbor, time in graph[node]: 
                if neighbor not in min_times:
                    heapq.heappush(min_heap, (time + time_k_to_node, neighbor))
                    
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1