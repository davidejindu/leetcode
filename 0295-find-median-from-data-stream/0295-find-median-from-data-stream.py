class MedianFinder:

    def __init__(self):
        self.largeHeap = []
        self.smallHeap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap,-num)

        # check if small heap len is greater 
        if len(self.smallHeap) - len(self.largeHeap) > 1:
            large_num = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap,large_num)
 
        #swap small heap great value with large heap great value
        if self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            large_num = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap,large_num)


        #check if large heap len is greater
        if len(self.largeHeap) > len(self.smallHeap):
            small_num = -heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap,small_num)
        

    def findMedian(self) -> float:

        if (len(self.largeHeap) + len(self.smallHeap)) % 2 == 0:
            return (self.largeHeap[0] + -self.smallHeap[0]) / 2
        else:
            return -self.smallHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()