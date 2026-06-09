class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        

        def maxHouse(nums):
            prev1, prev2 = 0, 0
            for i in range(len(nums)):
                current = max(prev1 + nums[i], prev2)

                prev1 = prev2
                prev2 = current

            return prev2

        return max(maxHouse(nums[1:]), maxHouse(nums[:-1]))