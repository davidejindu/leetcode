class Solution:
    def findMin(self, nums: List[int]) -> int:
        """

    4,5,6,7,0,1,2
            l       
              m
                r

    if mid > r that means the left portion contains higher values and pivot is to the right 

    else 
    that means the minimum can be mid or anything to left of mid so set r = mid




        """


        l, r = 0, len(nums) - 1


        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

            