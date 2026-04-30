class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """

        nums = [10,9,2,5,3,7,101,18]
                     i
                       j

        dp = [1,1,1,1,3,2,1,1]
                  i
                    j

        """

        dp = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

