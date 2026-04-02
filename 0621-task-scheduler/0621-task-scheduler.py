from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = {}

        for task in tasks:
            count_map[task] = 1 + count_map.get(task,0)

        maxHeap = [-count for count in count_map.values()]

        heapq.heapify(maxHeap)

        time = 0

        queue = deque()

        while maxHeap or queue:
            time +=1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)

                if count:
                    queue.append((count, time + n))

            if queue and queue[0][1] == time:
                count = queue.popleft()[0]
                heapq.heappush(maxHeap,count)

        return time
        

        