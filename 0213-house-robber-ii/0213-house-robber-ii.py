"""

so you cannot rob both the first and last houses 
or adjacent houses

so basically do house robber but with nums[:len(nums)-1] and nums[1:]


"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]


        def house_robber(houses):
            rob1, rob2 = 0, 0

            for money in houses:
                maxx = max(rob1 + money, rob2)

                rob1 = rob2
                rob2 = maxx

            return rob2

        return max(house_robber(nums[1:]), house_robber(nums[:len(nums) - 1]))

        