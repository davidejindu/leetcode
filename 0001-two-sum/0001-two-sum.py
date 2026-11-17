class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff_map = {}

        for index, value in enumerate(nums):
            diff = target - value

            if diff in diff_map:
                return [diff_map[diff], index]

            diff_map[value] = index

        return []
        