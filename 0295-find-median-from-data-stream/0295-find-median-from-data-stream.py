"""

find the median of a list

if its even get the average of the two middle values

if its odd just get the middle value


we are going to do this using two heaps

small heap
this will be a max heap so that when we get the first value we can check if its greater
than the large heap

large heap
this will me a min heap so when we get the first value we can confirm its smaller than the 
small heap

we will originally add the value to the smallHeap

we are going to check if the smallHeap is greater than 2 of the large Heap
if so we are going to pop and then add to the large heap the value from small heap

we are also going to check if the value in small heap is greater than value in large heap
if so we are going to pop and add that value to small heap

after that we will check if large heap is greater than small heap and if so we can pop 
from large heap and add it to small heap


2 3 4

smallHeap = [-2]
largeHeap = []

"""
class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -num)

        if len(self.smallHeap) - len(self.largeHeap) > 1:
            val = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        if self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            val = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        if self.largeHeap and len(self.largeHeap) > len(self.smallHeap):
            val = -heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, val)

        
        

    def findMedian(self) -> float:
        length = len(self.smallHeap) + len(self.largeHeap)

        if length % 2 != 0:
            return -self.smallHeap[0]
        else:
            return ((-self.smallHeap[0]) + self.largeHeap[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()