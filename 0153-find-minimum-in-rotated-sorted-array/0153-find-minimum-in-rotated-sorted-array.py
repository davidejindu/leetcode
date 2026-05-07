class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
    we know if m is greater than r then the minimum has to be in the left portion

    3,4,5,1,2
          l 
        m
          r

    if its not greater than it then m might be the minimum so set r to m to keep it in range






        """

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[r]