"""

-2,1,-3,4,-1,2,1,-5,4
                  ^
cur_sum = 1
max_sum = 6


"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)

            if cur_sum < 0:
                cur_sum = 0

        return max_sum

        