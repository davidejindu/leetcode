class MedianFinder:

    """
    medianFinder.addNum(1);    
    medianFinder.addNum(2);    
    medianFinder.findMedian();
    medianFinder.addNum(3);  
    medianFinder.addNum(0);  
    medianFinder.addNum(7);  
    medianFinder.findMedian(); 


    small_heap = [-1,0]
    large_heap = [2, , 7]


    create a small_heap and a large_heap
    they can't have more than 1 size length difference
    if they do then pop whichever one is greater by 2 value and add it to other heap
    small_heap is max heap and large_heap is min heap
    also all of the values in large heap has to be greater than all of values in small heap


    """
    def __init__(self):
        self.small_heap = []
        self.large_heap = []
        heapq.heapify(self.small_heap)
        heapq.heapify(self.large_heap)
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -num)

        if self.small_heap and self.large_heap:
            if -self.small_heap[0] > self.large_heap[0]:
                heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))

        if len(self.large_heap) - len(self.small_heap) > 1:
            heapq.heappush(self.small_heap, -heapq.heappop(self.large_heap))

        if len(self.small_heap) - len(self.large_heap) > 1:
            heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))




    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap):
            return (-self.small_heap[0] + self.large_heap[0]) / 2
        elif len(self.small_heap) > len(self.large_heap):
            return -self.small_heap[0]
        else:
            return self.large_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()