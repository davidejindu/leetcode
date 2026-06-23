"""

3,4,5,1,2
      l r
      m

1,2,3,4,5
l
    m
        r

if m is greater than r we can conclude it starts decreasing after m

if m is less than r set r = m








"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid

        return nums[l]

            
        