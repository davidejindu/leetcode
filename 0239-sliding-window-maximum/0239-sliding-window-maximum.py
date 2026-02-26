class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        make a deque for O(n)
        if the queue isnt empty and the last value in queue is less than nums[r] pop
        after that append to the queue so it has the top most value
        1,3,-1,-3,5,3,6,7  k = 3
          l
             r

        queue [1]        result = [3] 
        """

        queue = collections.deque()
        result = []
        l = 0

        for r in range(len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if r - l + 1 == k:
                result.append(nums[queue[0]])
                l +=1

            if l > queue[0]:
                queue.popleft()
            

        return result





     


        