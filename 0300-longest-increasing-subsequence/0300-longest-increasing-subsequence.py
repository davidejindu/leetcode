"""

10,9,2,5,3,7,101,18
           i
        j

1,1,1,2,2,1,1,1
      i
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])


        return max(dp)