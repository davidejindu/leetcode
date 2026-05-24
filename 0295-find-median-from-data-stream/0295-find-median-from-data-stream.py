class MedianFinder:

    def __init__(self):
        self.largeHeap = []
        self.smallHeap = []
        

    def addNum(self, num: int) -> None:

        heapq.heappush(self.smallHeap,-num)

        # check wrong values in heaps
        if self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            large_num = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap,large_num)

        # check too large heaps
        if len(self.smallHeap) - len(self.largeHeap) > 1:
            val = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)


        # chec if large heap is greater than small heap
        if len(self.largeHeap) > len(self.smallHeap):
            small_num = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -small_num)


    

    def findMedian(self) -> float:
        length = len(self.smallHeap) + len(self.largeHeap)

        if length % 2 != 0:
            return -self.smallHeap[0]
        else:
            return (-self.smallHeap[0] + self.largeHeap[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()