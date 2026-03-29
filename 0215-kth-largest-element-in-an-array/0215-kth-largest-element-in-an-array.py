class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
    change nums to be negative then make it a heap
    the keep popping until k and then return 



        """

        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapify(nums)

        result = 0
        for i in range(k):
            result = heapq.heappop(nums)

        return -result