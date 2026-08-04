class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        result = []

        for r in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[r], r))

            if r < k - 1:
                continue

            last_index = r - k + 1

            while maxHeap and maxHeap[0][1] < last_index:
                heapq.heappop(maxHeap)

            result.append(-maxHeap[0][0])


        return result
        