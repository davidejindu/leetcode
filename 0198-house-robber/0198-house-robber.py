class Solution:
    def rob(self, nums: List[int]) -> int:
        """

        1,3,3,1,0,0
        1
        3
        4


        """
        nums.append(0)
        nums.append(0)

        for i in range(len(nums) -3, -1, -1):
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])

        return nums[0]