class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        adj1 = nums[0]
        adj2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(nums[i] + adj1, adj2)

            adj1 = adj2
            adj2 = current 

        return adj2